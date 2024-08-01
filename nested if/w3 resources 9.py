print("program to accept a coordinate point in an XY coordinate system and determine in which quadrant the coordinate point lies")
x=int(input("Enter the x value: "))
y=int(input("Enter the y value: "))
if x>0 and y>0:
    print("It is first Quadrant...✨")
elif x<0 and y>0:
    print("It is Second Quadrant")
elif x<0 and y<0:
    print("It is Third Quadrant")
elif x>0 and y<0:
    print("It is Fourth Quadrant")
else:
    print("Coordinate doesnt exist in  Quadrant....")