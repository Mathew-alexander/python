print("program to find sum of digits of a number")
a=int(input("Enter the input value: "))
b=int(str(a)[:1])
c=int(str(a)[-1:])
sum=0
for i in range(1,-1,1):
    sum=sum+i
print(sum)