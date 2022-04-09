with open("8.txt", "r") as file: # read file into list of lists
    str0 =  file.readlines() # read lines into str0
    list1 = [] # make a blank list
    for i in str0: # nested for loop that reads the hex in the strings to bytes and then makes a list of them (list1)
        str1 =  bytes.fromhex(i)
        list2 = []
        for j in str1:
            list2.append(j)
        list1.append(list2)

list5 =[] # a blank list with an arbitrary number
for ciphertext in list1: # for each entry in the list
    z = 0
    for j in range(0,10): # nested for loop that compares 16 bytes segments of the cipher text to each other
        for k in range(0,10):
            if (ciphertext[16*j:16*j+16]) == (ciphertext[16*k:16*k+16]):
                z += 1
    list5.append(z) # append the number of matches to list5

index1 = (list5.index(max(list5))) # find the position of the largest number of similarities
print(list5[index1]) # print the value of the largest number of similarities
print(str0[132]) #print index in original list, yielding answer
