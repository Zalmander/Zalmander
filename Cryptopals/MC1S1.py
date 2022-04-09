# This simple script converted hex to base64

import codecs # import libs

def hextob64(hex): #def function to convert
    b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
    print(b64)

hex = input("enter hex") # assign user input to var hex
hextob64(hex) # call function
