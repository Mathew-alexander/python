print("program to enter student marks and find percentage and grade")
a=float(input("Enter the first subject mark: "))
b=float(input("Enter the secon\d subject mark: "))
c=float(input("Enter the third subject mark: "))
d=float(input("Enter the fourth subject mark: "))
e=float(input("Enter the fifth subject mark: "))
percentage=(a+b+c+d+e)/5.0
print("TOTAL PERCENTAGE IS=",percentage)
if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")