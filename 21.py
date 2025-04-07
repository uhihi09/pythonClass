height = int(input("키(cm):"))
weight = int(input("체중(kg):"))
print("##########")
if height >= 130 and height < 190:
    if weight >= 25 and weight < 100:
        print("이용 가능")
    else:
        print("이용 불가능")
