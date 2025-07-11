a = input()
b = int(input())
cnt1 = []
cnt2 = []
ans = 0
ans1 = ["Head","Top","Bottom","Shoes","Gloves","Belt"]
ans1_dic = {"Head":0,"Top":1,"Bottom":2,"Shoes":3,"Gloves":4,"Belt":5}
ans2 = []
ans3 = []
ans3_set = set()
wow = 0
for i in range(b):
    cnt1.append(input().split())
c = int(input())
for i in range(c):
    cnt2.append(input().split())
for i in range(len(cnt1)):
    for ii in range(len(cnt2)):
        if i == ii:
            if cnt1[i][1] == cnt2[ii][1]:
                if int(cnt2[ii][cnt2[ii].index(a)+1]) >= int(cnt1[i][cnt1[i].index(a)+1]):
                    cnt1[i]= cnt2[ii]
for i in range(len(cnt1)):
    for ii in range(len(cnt2)):
        if i == ii:
            if cnt1[i][1] != cnt2[ii][1]:
                if cnt2[i][1] == "Head":
                    cnt1.insert(0,cnt2[ii])
                elif cnt2[i][1] == "Top":
                    cnt1.insert(1,cnt2[ii])
                elif cnt2[i][1] == "Bottom":
                    cnt1.insert(2,cnt2[ii])
                elif cnt2[i][1] == "Shoes":
                    cnt1.insert(3,cnt2[ii])
                elif cnt2[i][1] == "Gloves":
                    cnt1.insert(4,cnt2[ii])
                elif cnt2[i][1] == "Belt":
                    cnt1.insert(5,cnt2[ii])
cnt1.sort(key=lambda x: ans1_dic[x[1]])
for i in cnt1:
    e = i[1]
    if e not in ans3_set:
        ans3.append(i)
        ans3_set.add(e)
for i in range(len(ans3)):
    print(*ans3[i][:2],end=" ")
    print(*ans3[i][ans3[i].index(a):cnt1[i].index(a)+2])
for i in range(len(ans3)):
    ans += int(ans3[i][ans3[i].index(a)+1])
if b != 0:
    print(f"{a} Total: {ans}")