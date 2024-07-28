print("program to calculate electricity bill")
a=float(input("Enter the total units consumed: "))
if a <= 50:
    amount=a*0.50
    sur_charge = amount * 0.20
    total_amt= amount + sur_charge
    print("ELECTRICITY BILL= ",total_amt)
elif a <=150:
    amount= 25 + ((a-50)*0.75)
    sur_charge = amount * 0.20
    total_amt= amount + sur_charge
    print("ELECTRICITY BILL= ",total_amt)
elif a<=250:
    amount=100+((a-150)*1.20)
    sur_charge = amount * 0.20
    total_amt= amount + sur_charge
    print("ELECTRICITY BILL= ",total_amt)
elif a>250:
    amount=220+((a-250)*1.50)
    sur_charge = amount * 0.20
    total_amt= amount + sur_charge
    print("ELECTRICITY BILL= ",total_amt)
