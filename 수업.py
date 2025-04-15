id_db = ["kkk", 'iii', "jjj"]  
id = input("id: ")
a = []
if id in id_db:
	print("이미 가입된 ID입니다.")
elif id not in id_db:
	print(f"{id}로 회원가입을 진행합니다.")
	print(f"{id}")
	a = input("pw(!,@,# 중 한 개 이상 포함): ").split(" ")
	if "!"in a or "@" in a or "#" in a:
		print("회원가입 완료")
	else:
		print("회원가입 취소")