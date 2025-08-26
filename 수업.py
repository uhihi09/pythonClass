a = list(input())
b = list(input())
ans = ""
for i in range(len(a)):
    ans += max(a[i], b[i])
print(ans)