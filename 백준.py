a = list(map(input()))
b = int(a)
if 7 not in a and b%7 != 0:
    print(0)
elif 7 not in a and b%7 == 0:
    print(1)
elif 7 in a and b%7 != 0:
    print(2)
else:
    print(3)