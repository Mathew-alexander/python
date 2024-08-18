print("program to find sum of first and last digit of any number")
a=int(input("Enter the input number: "))
b=int(str(a)[:1])
c=int(str(a)[-1:])
print("first digit is=",b)
print("Last digit is=",c)
sum=b+c
print("sum:=",sum)