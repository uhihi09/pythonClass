a = int(input())
for i in range(a):
    b = list(input().split())
    cnt = b[0]
    b[1] = int(b[1])
    b[2] = int(b[2])
    cnt = list(cnt)
    del cnt[b[1]:b[2]]
    print("".join(map(str, cnt)))