n = int(input())
p = int(input())
if n >= 5 and n < 10:
    print(p-500)
elif n >= 10 and n < 15:
    print(int(p*(90/100)))
elif n >= 15 and n < 20:
    print(p-2000)
elif n >= 20:
    print(int(p*(75/100)))
else:
    print(p)