def sub_1(lst):
    mylst = list(range(7,11))
    print(f"sub_1 함수 리스트: {mylst}")
def sub_2(lst):
    global mylst
    mylst = list(range(1,5))
    print(f"sub_2 함수 리스트: {mylst}")

mylst = list(range(10,50,10))
sub_1(mylst)
sub_2(mylst)
print(f"메인함수 리스트: {mylst}")