a,b = map(int, input().split(","))
a = a//10000
if b == 1 or b == 2:
    c = 1900 + a
    print(f"현재나이는 {2026-c}살 입니다.")
elif b == 3 or b ==4:
    c = 2000 + a
    print(f"현재나이는 {2026-c}살 입니다.")
else:
    print("존재하지 않습니다")