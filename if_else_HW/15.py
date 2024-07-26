print("program to check whether triangle is valid or not if sides are given")
side1=int(input("Enter the first side: "))
side2=int(input("Enter the second side: "))
side3=int(input("Enter the third side: "))
if (side1 + side2) >side3:
    print("Triangle is valid..")
elif(side2+side3)>side1:
    print("Triangle is valid..")
elif(side1+side3)>side2:
    print("Triangle is valid..")
else:
    print("Triangle is not valid..")