a = int(input("행 수: "))
for i in range(1,a+1):
    for ii in range(a-i):
        print(" ",end="")
    for iii in range(i*2-1):
        print("*",end="")
    print()