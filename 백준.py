import sys
input = sys.stdin.readline
a,b = map(int,input().split())
cnt1 = []
cnt2 = []
ans = []
for i in range(a):
    cnt1.append(input())
for ii in range(b):
    cnt2.append(input())
for i in cnt1:
    for ii in cnt2:
        if i == ii:
            ans.append(i)
ans.sort()
print(len(ans))
for i in ans:
    print(i)