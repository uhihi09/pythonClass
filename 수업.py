def fac(a):
    if a <= 1:
        return 1
    else:
        return a * fac(a-1)
def gcd(a,b):
    if b== 0:
        return a
    else:
        return gcd(b,a%b)
def wow(a):
    tri = [[]for i in range(a)]
    for i in range(a):
        for ii in range(i+1):
            if i == 0 or ii == 0 or i == ii:
                tri[i].append(1)
            else:
                tri[i].append(tri[i-1][ii]+tri[i-1][ii-1])
    for i in tri:
        print(*i)
def setli(a):
    b = set(a)
    print(b[0]) # 에러남 왜냐하면 셋은 인덱스로 접근 불가 list()한후 접근 ㄱㄱ, 중복 없앨때도 사용, set 더할때 .update
def dic():
    a = int(input())
    b = {"준영":95,"하예":78,"가윤":82,"성희":51,"미연":94}
    if a in b.values():
        print(b[a])
    else:
        print("X")
print(fac(1))
print(fac(0))
print(gcd(10,82174398124791234))