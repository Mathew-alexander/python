print("program to print all even numbers from 1 to n")
a=int(input("Enter the limit value: "))
for i in range(1,a+1,1):
    if i%2==0:
        print(i)