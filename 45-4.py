a = int(input("행 수: "))
for i in range(a,0,-1):
    for ii in range(a-i):
        print(" ",end="")
    for iii in range(i):
        print("*",end="")
    print()