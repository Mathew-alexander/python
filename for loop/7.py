print("program to find sum of even numbers between 1 to n")
a=int(input("Enter the n value: "))
sum=0
for i in range(1,a+1,1):
    if i%2==0:
        sum=sum+i
print("sum is",sum)