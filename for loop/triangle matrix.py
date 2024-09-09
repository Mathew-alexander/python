matrix=int(input("Enter the number: "))+1
space=matrix-2
for i in range(1, matrix):
    print(" " * space, end="")
    print("# " * i)
    space -= 1