a = int(input("행 수: "))
for i in range(1,a+1):
    for ii in range(a-i):
        print(" ",end="")
    for iii in range(i*2-1):
        print("*",end="")
    print()
for vi in range(a-1,0,-1):
    for v in range(a-vi):
        print(" ",end="")
    for iv in range(vi*2-1):
        print("*",end="")
    print()