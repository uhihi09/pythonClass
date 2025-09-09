a = input()
a = a.upper()
wow = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cnt = []
cnt1 = []
for i in wow:
    cnt.append(a.count(i))
    cnt1.append(wow.index(i))
ans = cnt.count(max(cnt))
if ans == 1:
    print(wow[cnt1.index(cnt.index(max(cnt)))])
else:
    print('?')