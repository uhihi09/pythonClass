def math(a):
    if int(a) < 0:
        return f"{a}의 절댓값은 {a*-1}입니다"
    else:
        return f"{a}의 절댓값은 {a}입니다"
a = float(input("실수를 입력하시오.: "))
print(math(a))