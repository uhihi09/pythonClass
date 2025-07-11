def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
ans = []
cnt = []
ans1 = []
while True:
    try:
        a = list(map(int, input().split()))
        ans.append(a)
    except EOFError:
        for i in range(len(ans)):
            for ii in range(len(ans[i])):
                cnt.append(ans[i][ii])
        for i in range(len(cnt)):
            for ii in range(i+1,len(cnt)):
                ans1.append(gcd(cnt[i],cnt[ii]))
        print(max(ans1))
        break