from Crypto.Cipher import AES
import base64

with open("7.txt", "r") as file:
    str1 = base64.b64decode(file.read())

obj = AES.new(b'YELLOW SUBMARINE', AES.MODE_ECB)

print(obj.decrypt(str1).decode("ascii"))
