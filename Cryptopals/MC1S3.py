# this script decrypts a single character XOR encrypted string

def hextointlist(): # this function splits and converts the hex encoded string into a list of integers
    hex_val = input("enter hex value")
    hex_list = [hex_val[i:i+2] for i in range(0, len(hex_val), 2)]
    int_list=[]
    for j in hex_list:
        int_list.append(int(j,16))
    return int_list

def score(string1): # this function uses character frequency to "score" english plaintext
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
    bad1 = string1.count('!')
    score = e+t+a+o+i+n+s+h+r+d+l+u-(100*bad1)
    return score

def sbXOR_dtect(int_list): # single byte XOR; takes a list of integers, XORs them with each possible integer in the hex format (0-255); then scores and returns the top score and result 
    ath = 0
    all_ints = [*range(0,255,1)]
    for i in all_ints:
        XORd = []
        for j in int_list:
            XORd.append(chr(i ^ j))
        XORd_score = score(''.join(XORd))
        print(XORd,chr(i))
        if XORd_score > ath:
            ath = XORd_score
            realone = ''.join(XORd)
            cypher_char = chr(i)
    return realone, cypher_char

a = hextointlist()
print(sbXOR_dtect(a))
