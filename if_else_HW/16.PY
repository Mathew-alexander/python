print("program to check whether triangle is equilateral, scalene or isosceles")
angle1=int(input("Enter the first angle: "))
angle2=int(input("Enter the second angle: "))
angle3=int(input("Enter the third angle: "))
if angle1==angle2 and angle2==angle3:
    print("IT IS A EQUILATERAL TRIANGLE....")
elif angle1==angle2 or angle1==angle3 or angle2==angle3:
    print("IT IS A ISOSCELES TRIANGLE..")
else:
    print("IT IS A SCALENE TRIANGLE...")
