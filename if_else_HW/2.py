print("Finding the greatest number")
a = input("Enter your first number: ")
b = input("Enter your second number: ")
c = input("Enter your third number: ")
if a>b and a>c:
    print(a)
    print("a is greater")
elif b>a and b>c:
    print(b)
    print("b is greater")    
else:
    print(c)
    print("c is greater")