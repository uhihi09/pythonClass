def fun_f(n):
    if n < 2:
        return 1
    else:
        return n * fun_f(n-1)
print(fun_f(1))
print(fun_f(10))
a = int(input("자연수: "))
print(fun_f(a))