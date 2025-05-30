f=open('data_1.txt','w')

n = int(input('[1] 출석입력 [2] 추가 입력 [3] 기록 보기 [4] 종료'))
if n == 1:
    while True:
        line= input('출석 입력: ')
        if line == '':
            break
        f.write(line)
elif n ==2:
    while True:
        line= input('추가 입력: ')
        if line == '':
            break
        f.write(line)
elif n == 3:
    print("기록 보기")
    while True:
        line=f.readline()
        if line == '':
            break
        print(line,end="")
elif n == 4:
    print("종료")
    f.close