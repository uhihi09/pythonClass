hap = []
while True:
    try:
        a = float(input("점수: "))
        hap.append(a)
    except:
        break
print("==========")
print(f"합계: {sum(hap)}")
print(f"평균: {sum(hap)/len(hap)}")