print("program to check whether triangle is valid or not if angles are given")
angle1=int(input("Enter the first angle: "))
angle2=int(input("Enter the second angle: "))
angle3=int(input("Enter the third angle: "))
sum=angle1 + angle2 + angle3
if sum==180 and angle1 > 0 and angle2 >0 and angle3 >0:
    print("IT IS A TRIANGLE........")
else:
    print("IT IS NOT A TRIANGLE")