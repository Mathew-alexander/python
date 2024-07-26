print("program to find number of days in month")
a=int(input("Enter the month number: "))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("IT HAS 31 DAYS...")
elif a==4 or a==6 or a==9 or a==11:
    print("IT HAS 30 DAYS...")
elif a==2:
    print("IT HAS 28/29 DAYS")
else:
    print("ENTER MONTH NUMBER")