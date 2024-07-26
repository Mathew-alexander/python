print("checking whether the year is leap year or not?")
year=int(input("Enter the year: "))
if  year%400==0:
    print(year)
    print("This year is a Leap year")
else:
    print(year)
    print("This year is not a Leap year")