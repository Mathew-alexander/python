print("check whether a character is alphabet, digit or special character")
a=input("Enter the character: ")
if (a>='a' and a<='z') or (a>='A' and a<='Z'):
    print("It is a alphabet")
elif a>='0' and a<='9':
    print("It is a DIGIT")
else:
    print(a)
    print("it is a special character")