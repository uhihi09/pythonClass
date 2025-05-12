def maxp(n,m):
    if n >= m:
        cnt = n
    else:
        cnt = m
    return cnt

print(f"큰 수: {maxp(10,20)}")

a,b = map(int, input().split())
print(f"큰 수:{maxp(a,b)}")