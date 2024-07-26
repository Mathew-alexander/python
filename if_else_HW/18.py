print("program to calculate profit or loss")
a=int(input("Enter the cost price: "))
b=int(input("Enter the selling price; "))
amount1 = b -a
amount2=a-b
if b>a:
    print("profit= ",amount1)
elif a>b:
    print("loss= ",amount2)
else:
    print("there is no profit and loss....")