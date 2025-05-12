print("## 예외처리 1 ##")
while True:
    try:
        n_1 = int(input("숫자: "))
    except ValueError:
        print("숫자만 입력하세요.")
    else:
        print(n_1)
        break