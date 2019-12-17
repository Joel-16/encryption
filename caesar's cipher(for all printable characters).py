# finding the mirror image of an alphabet
#caesar's cipher
#str_rotate
user=input("enter te word you want to find the cipheer value ")
dist=int(input("enter the respective distance "))
code=""
for letters in user:
    ordval=ord(letters)
    cipher=ordval+dist
    if cipher>256:
        cipher=30+dist-(256-ordval+1)
    code+=chr(cipher)
print(code)
