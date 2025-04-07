import random

print("<<컴퓨터가 생각한 1~20 숫자 맞추기>>")
a = random.randint(1,20)
b = 0
while a != b:
    b = int(input("숫자입력(종료0):"))
    if b == 0:
        break
    elif a > b:
        print("더 큰 숫자 입력!")
        continue
    elif a < b:
        print("더 작은 숫자 입력!")
        continue
    elif a == b:
        print("정답!!")