def loadtxttovar(txt):
    with open(txt) as f:
        lines = f.read().splitlines()
    return lines

def hextointlist(hex_val):
    #hex_val = input("enter hex value")
    hex_list = [hex_val[i:i+2] for i in range(0, len(hex_val), 2)]
    int_list=[]
    for j in hex_list:
        int_list.append(int(j,16))
    return int_list

def hexstrlisttoint(hexstring_list):
    masterlist = []
    for i in hexstring_list:
        newintlist = hextointlist(i)
        masterlist.append(newintlist)
    return masterlist

def score(string1):
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
    bad1 = string1.count('}')
    bad2 = string1.count('{')
    bad3 = string1.count('>')
    bad4 = string1.count('<')

    score = e+t+a+o+i+n+s+h+r+d+l+u-bad1*100-bad2*100-bad3*100-bad4*100
    return score

def sbXOR_dtect(int_list):
    ath = 0
    all_ints = [*range(0,255,1)]
    for i in all_ints:
        XORd = []
        for j in int_list:
            XORd.append(chr(i ^ j))
        XORd_score = score(''.join(XORd))
        if XORd_score > ath:
            ath = XORd_score
            realone = ''.join(XORd)
            #cypher_char = chr(i)
    return realone#, cypher_char

def sbXOR_dtect_multiple(listoflists):
    listofrealones = []
    for i in listoflists:
        listofrealones.append(sbXOR_dtect(i))
    print(listofrealones)
    hiscore = 0
    winner = 'asd'
    for j in listofrealones:
        scoreresult = score(j)
        if scoreresult > hiscore:
            hiscore = scoreresult
            winner = j
    return winner

stringslist = loadtxttovar('4.txt')
intlistofstrings = hexstrlisttoint(stringslist)
print(sbXOR_dtect_multiple(intlistofstrings))
