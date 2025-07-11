import sys
input = sys.stdin.readline
def love(a):
    ans = []
    for i in range(1,a+1):
        if a % i == 0:
            ans.append(i)
    return ans[-2]
def pls(b):
    if b == 1:
        return b
    else:
        return b + pls(love(b))
a = int(input())
print(pls(a))