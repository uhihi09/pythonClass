a,b,c = map(int, input("세 수를 입력하세요:").split())
if a>b and a>c and c>b:
    print(f"두번째 수는 {c} 입니다")
elif b>a and b>c and a>b:
    print(f"두번째 수는 {a} 입니다")
else:
    print(f"두번째 수는 {b} 입니다")