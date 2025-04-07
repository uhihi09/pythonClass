a = int(input("자연수 입력: "))
b = 1
for i in range(1,a+1):
    b *= i
print(f"{a}!은 {b}")