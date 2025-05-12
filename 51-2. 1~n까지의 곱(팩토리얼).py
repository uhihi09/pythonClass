def fun_fact(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
print(fun_fact(5))
print(fun_fact(10))