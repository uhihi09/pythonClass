a = list(input())
b = int(input())
for i in a:
    if (ord(i) > 90 and ord(i) < 97) or ord(i) < 65 or ord(i) > 122:
        print(i,end="")
    elif ord(i)+b > 90 and ord(i)+b < 97:
        i = ord(i)-(25-b+1)
        print(chr(i),end="")
    else:
        i = ord(i)+b
        print(chr(i),end="")