import sys
import math
input = sys.stdin.readline
# def pac(n):
#     wow = {}
#     if n in wow:
#         return wow[n]
#     elif n <= 1:
#         return 1
#     else:
#         wow[n] = n * pac(n-1)
#         return wow[n]
a,b = input().split()
b = int(b)
cnt = a
ans = 0
for i in range(b-1):
    for ii in range(len(cnt)):
        ans += math.factorial(int(cnt[ii]))
    cnt = str(ans)
    ans = 0
print(cnt)