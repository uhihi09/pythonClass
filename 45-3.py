a = int(input("행 수: "))
for i in range(a-1,-1,-1):
    for ii in range(i-1,-1,-1):
        print(" ",end="")
    for iii in range(a-i):
        print('*',end="")
    print()