with open("8.txt", "r") as file:
    str0 =  file.readlines()
    #print(str0)
    list1 = []
    for i in str0:
        str1 =  bytes.fromhex(i)
        list2 = []
        for j in str1:
            list2.append(j)
        list1.append(list2)

list5 =[]
for ciphertext in list1:
    z = 0
    for j in range(0,10):
        for k in range(0,10):
            if (ciphertext[16*j:16*j+16]) == (ciphertext[16*k:16*k+16]):
                z += 1
    list5.append(z)

print(list5.index(max(list5)))
print(list5[132])
print(str0[132])
