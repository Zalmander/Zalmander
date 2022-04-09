# This script takes two equal-length buffers and produces their XOR combination

def hexdecode(): # function to decode hex
    decoded = int(input("enter hex"),16)
    return decoded

decoded_hex1 = hexdecode() # decode hex 1
decoded_hex2 = hexdecode() # decode hex 2

print(hex(decoded_hex1^decoded_hex2)[2:]) # xor the two strings and print

