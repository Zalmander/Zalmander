# goal is to implement repeating key XOR

def repeating_key_XOR(unencrypted_str, key): # takes a string and a key and sequentially applies each byte of the key to the plaintext
    counter=0
    encrypted_list = []
    for j in unencrypted_str:
        encrypted_list.append(hex(ord(key[counter])^ord(j)))
        counter = (counter + 1 ) % len(key)
    return (''.join(encrypted_list)).replace('0x',"")

print(repeating_key_XOR("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",'ICE'))
