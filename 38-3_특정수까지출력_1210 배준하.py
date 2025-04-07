print("단을 표준입력으로 받아 구구단 출력")
a = int(input("몇 단?: "))

print(f"==={a}단===")
for i in range(1,10):
    print(f"{a} * {i} = {a*i}")