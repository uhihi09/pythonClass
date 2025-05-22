matrix1 = []
matrix2 = []
ans = []
for i in range(2):
    a = list(map(int,input().split()))
    matrix1.append(a)
for i in range(2):
    b = list(map(int,input().split()))
    matrix2.append(b)
for i in range(2):
    row = []
    for ii in range(4):
        row.append(matrix1[i][ii]*matrix2[i][ii])
    ans.append(row)
for i in ans:
    print(*i)