sum = 0
count = 0
score = 0
while score != -1:
    score = float(input("점수: "))
    if score == -1:
        break
    sum = sum + score
    count = count + 1
avg = sum/count
print("=========")
print(f"합계: {sum}")
print(f"평균: {avg}")