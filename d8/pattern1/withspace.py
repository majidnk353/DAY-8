row=5
for n in range(row):
    for space in range(4-n):
        print(" ",end=" ")
    for i in range(n+1):
        print("*",end=" ")
    print()
