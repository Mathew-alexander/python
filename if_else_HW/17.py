print("program to find all roots of a quadratic equation")
a=int(input("Enter the a value: "))
b=int(input("Enter the b value: "))
c=int(input("Enter the c value: "))
d=(b*b)-(4*a*c)
print("d=",d)
if d > 0:
    root1 = (-b + (d)) / (2*a)
    root2 = (-b - (d)) / (2*a)
    print("root1=",root1,)
    print("root2",root2)
elif d==0:
    root1 = root2 = -b / (2*a)
    print("Two distinct and real roots exists",root1 ,root2)
elif d < 0:
    root1 = root2 = -b / (2 * a)
    imaginary = (-d) / (2 * a)
    print("Two distinct complex roots exists:",root1, imaginary, root2, imaginary)