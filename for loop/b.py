a=int(input("Enter the n number: "))
sum=0
pro=1
for i in range(1,a+1,1):
    num=int(input("Enter the value: "))
    sum=sum+num
    pro=pro*num
print("sum= ",sum)
print("product= ",pro)