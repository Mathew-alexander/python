print("program to enter basic salary and calculate gross salary of an employee")
basic=float(input("Enter the basic salary: "))
if basic <= 10000:
    da  = basic * 0.8
    hra = basic * 0.2
    print("da= ",da)
    print("hra= ",hra)
elif basic <= 20000:
    da  = basic * 0.9
    hra = basic * 0.25
    print("da= ",da)
    print("hra= ",hra)
else:
    da  = basic * 0.95
    hra = basic * 0.3
    gross = basic + hra + da
    print("GROSS SALARY OF EMPLOYEE = ", gross)