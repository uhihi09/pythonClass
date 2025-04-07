import random

com1 = random.randrange(1,7)
com2 = random.randrange(1,7)
a = list(map(int, input().split()))
if a in com1 and a in com2:
    print("1등")
elif a in com1 or a in com2:
    print("2등")
else:
    print("3등")