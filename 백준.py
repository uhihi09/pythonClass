n,m,k = map(int,input().split())
ans1 = []
ans2 = []
cnt = 0
for i in range(m):
    ans1.append(True)
for i in range(n-m):
    ans1.append(False)
for i in range(k):
    ans2.append(True)
for i in range(n-k):
    ans2.append(False)
for i in range(n):
    if ans1[i] == ans2[i]:
        cnt += 1
print(cnt)