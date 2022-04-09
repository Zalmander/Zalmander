# goal is to implement PKCS#7 padding

blocksize = 20 # want the block size to be 20
plaintext = "YELLOW SUBMARINE" # input is only 16 characters

encoded_plaintext = plaintext.encode('utf-8') #encode plaintext
hex_plaintext = encoded_plaintext.hex() # convert to hex
nBytes = (int(len(hex_plaintext)/2)) # find number of bytes
if nBytes == blocksize:
    print("no padding needed ", hex_plaintext)
else:
    byteDifference = blocksize - nBytes
    for i in range(byteDifference):
        hex_plaintext = hex_plaintext + '0' + str(byteDifference) # padding step
print("padded", hex_plaintext)
