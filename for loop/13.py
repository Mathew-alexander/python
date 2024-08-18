print("program to swap first and last digit of a number")
a=int(input("Enter the input number: "))
b=int(str(a)[:1])
c=int(str(a)[-1:])
b,c=c,b
print("swapped numbers are:",end=" ")
print(b,end=" ")
print(c)