import random

a = int(input("입력(1.가위 2.바위 3.보):"))
b = [1,2,3]
com = random.randint(1,3)
if com == 1:
    if a == 1:
        print("user:가위","com:가위","->","비겼음")
    elif a == 2:
        print("user:바위","com:가위","->","이겼음")
    elif a == 3:
        print("user:보","com:가위","->","졌음")
if com == 2:
    if a == 1:
        print("user:가위","com:바위","->","졌음")
    elif a == 2:
        print("user:바위","com:바위","->","비겼음")
    elif a == 3:
        print("user:보","com:바위","->","이겼음")
if com == 3:
    if a == 1:
        print("user:가위","com:보","->","이겼음")
    elif a == 2:
        print("user:바위","com:보","->","졌음")
    elif a == 3:
        print("user:보","com:보","->","비겼음")