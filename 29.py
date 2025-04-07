a = 1
while a !=0:
    a = int(input("입력: "))
    if a != 0 and a%5 == 0:
        print("5의 배수 입니다.")
    elif a != 0 and a%5 != 0:
        print('5의 배수가 아닙니다.')
print("프로그램 종료")