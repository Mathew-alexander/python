print("program to print multiplication table of a given number")
a=int(input("Enter the multiplication table value: "))
for i in range(1,11,1):
    mul=a*i
    print(mul,end=" ")