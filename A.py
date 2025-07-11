d = ["ALT","B1ND","SAMDI","Louter","CNS","MODI","DUCAMI","Chatty"]
a = int(input())
for i in range(a):
    b = int(input())
    c = list(input().split())
    cnt = 0
    for ii in c:
        for iii in d:
            if ii == iii:
                cnt += 1
    if cnt != 1:
        print("No")
    else:
        print("Yes")