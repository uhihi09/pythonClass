name = ["김용휘", "박원준", "백승준", "배준하"]
name2 = ["이원재", "안현우", "우병헌"]
name.append("우승하")
print(name)
name.insert(3,"김규민")
print(name)
name.extend(name2)
print(name)
name.insert(1,"김규민")
print(name)
name.remove("김규민")
print(name)
del name[4]
print(name)
name.pop()
print(name)
a = [6, 3, 9]
print('a:', a)
a.sort(reverse=True) # 원본을 역정렬하고 수정
print('-----수행 후-----')
print('a:', a)
i = {"귀여움":"백승준","똑똑함":"박원준"}
print(i["똑똑함"])