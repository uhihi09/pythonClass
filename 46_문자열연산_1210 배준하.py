a = input("문장 입력:")
print("####################")
print(f"대문자 변환: {a.upper()}")
print(f"소문자 변환: {a.lower()}")
print(f"문자열 길이: {len(a)}")
print(f"공백으로 분리: {a.split()}")
print(f'마침표로 분리: {a.split(".")}')
print(f'o의 위치: {a.index("o")}')
print(f'o의 개수: {a.count("o")}')
b = a.replace("Python","AI")
print(f"Python을 AI로 교체: {b}")