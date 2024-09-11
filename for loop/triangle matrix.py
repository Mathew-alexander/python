# matrix=int(input("Enter the number: "))+1
# space=matrix-2
# for i in range(1, matrix):
#     print(" " * space, end="")
#     print("# " * i)
#     space -= 1



matrix=int(input("Enter the number: "))
space=matrix
for i in range(1,matrix+1):
    print(" "*space,end="")
    print("* "*i)
    space-=1