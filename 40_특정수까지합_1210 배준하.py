import random

while True:
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = 0
    if a > b:
        for i in range(b,a+1):
            c += i
        print(f"{a} ~ {b} => {c}")
    elif b > a:
        for i in range(a,b+1):
            c += i
        print(f"{b} ~ {a} => {c}")
    elif a == b:
        print(f"{a} ~ {b} => {b}")
        break  