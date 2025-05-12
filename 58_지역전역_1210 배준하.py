def sub1(x):
    a = x + 100
    return a
def sub2(x):
    global a
    a = x+100
    return a
a = 10
print(sub1(a))
print(a)
print(sub2(a))
print(a)