import base64 # import libs
import numpy as np

def loadtxttovar(txt): #loads text file as variable
    with open(txt) as f:
        lines = f.read()
    return lines

def b64decode(text): # decodes base64 to ascii
    lines = loadtxttovar(text)
    lines_bytes = lines.encode('ascii')
    decodedBytes = base64.b64decode(lines_bytes)
    ciphertext = decodedBytes.decode('ascii')
    return ciphertext

def hamm_dist_cipher(ciphertext): # used to find the hamming distance between two bytes
    keysize_hd = []
    for i in range (2,40,1):
        toBeSummed=[]
        for j in range(2,40,1):
            text_list3 = ciphertext[(j-2)*i:(j-1)*i]
            text_list4 = ciphertext[(j-1)*i:j*i]
            counter = 0
            for (k,l) in zip(text_list3,text_list4):
                x = (bin(ord(k)^ord(l))[2:])
                for m in x:
                    if m == '1':
                        counter += 1
            toBeSummed.append(counter)
        keysize_hd.append([(sum(toBeSummed)/len(toBeSummed))/i, i])
    edit_dist = 100
    final_keysize = 0
    for n,p in keysize_hd:
        if n < edit_dist:
            edit_dist = n
            final_keysize = p
    return final_keysize

def keysizeblocks(ciphertext, keysize): # used to split ciphertext into blocks of a given size
    ciphertext_list = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
    int_list = []
    for j in ciphertext_list:
        tiny_list = []
        for k in j:
            tiny_list.append(ord(k))
        int_list.append(tiny_list)
    return int_list

def transpose_list(toBeTransposed,m): # transposes a list
    transposed = []
    for i in range(0,m,1):
        row = []
        for l1 in toBeTransposed:
            if m > len(l1):
                continue
            else:
                row.append(l1[i])                
        transposed.append(row)
    return transposed

def sbXOR_dtect_multiple(transList): # takes a list of list of integers, runs them thru sbXOR_dtect_char and returns the results in a list
    listCypherChars = []
    for sublist in transList:
        listCypherChars.append(sbXOR_dtect_char(sublist))
    return ''.join(listCypherChars)

def sbXOR_dtect_char(int_list): # used to detect which single byte something is encrypted with
    all_time_high = -1000000
    ascii_ints = [*range(0,255,1)]
    for i in ascii_ints:
        XORd = []
        for j in int_list:
            #print(j)
            XORd.append(chr(i ^ j))
            #print((chr(i ^ j)))
        #print(''.join(XORd)[0], chr(i))
        XORd_score = score(''.join(XORd))
        if XORd_score > all_time_high:
            all_time_high = XORd_score
            decryptedString = ''.join(XORd)
            cypher_char = chr(i)
    #return decryptedString
    return cypher_char

def score(string1): # used to count letters and discount not english characters
    e = string1.count('e')
    t = string1.count('t')
    a = string1.count('a')
    o = string1.count('o')
    i = string1.count('i')
    n = string1.count('n')
    s = string1.count('s')
    h = string1.count('h')
    r = string1.count('r')
    d = string1.count('d')
    l = string1.count('l')
    u = string1.count('u')
    bad1 = string1.count('~')
    bad2 = string1.count('Î')
    bad3 = string1.count('Ó')
    bad4 = string1.count('Ï')
    bad5 = string1.count('#')
    bad6 = string1.count('&')
    score = e+t+a+o+i+n+s+h+r+d+l+u-(100*bad1)-(100*bad2)-(100*bad3)-(100*bad4)-(100*bad5)-(100*bad6)
    return score

def repeating_key_XOR(unencrypted_str, key): # takes a string and a key and sequentially applies each byte of the key to the plaintext
    counter=0
    encrypted_list = []
    for j in unencrypted_str:
        encrypted_list.append(chr(ord(key[counter])^ord(j)))
        counter = (counter + 1) % len(key)
    return (''.join(encrypted_list)).replace('0x',"")

ciphertext = b64decode('6.txt')
m = hamm_dist_cipher(ciphertext)
listofints = keysizeblocks(ciphertext,m)
transposed_list = transpose_list(listofints,m)
key = sbXOR_dtect_multiple(transposed_list)
print(repeating_key_XOR(ciphertext,key))
