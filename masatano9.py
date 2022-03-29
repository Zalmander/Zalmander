blocksize = 20#int(input('enter length'))
plaintext = "YELLOW SUBMARINE"#input('plaintext?')

encoded_plaintext = plaintext.encode('utf-8')
hex_plaintext = encoded_plaintext.hex()
nBytes = (int(len(hex_plaintext)/2))
if nBytes == blocksize:
    print("no padding needed ", hex_plaintext)
else:
    byteDifference = blocksize - nBytes
    for i in range(byteDifference):
        hex_plaintext = hex_plaintext + '0' + str(byteDifference)
print("padded", hex_plaintext)
