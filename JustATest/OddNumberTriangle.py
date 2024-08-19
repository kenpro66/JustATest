rows = 6   # set the number of rows
num = 1    # set the first number
for i in range(rows):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(i+1):
        print(num, end=" ")
        num += 2
    print()
