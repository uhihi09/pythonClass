from turtle import *

def input_data(): #시작점 입력 받기
    a,b = map(int, input("x좌표,y좌표: ").split(","))
    return a,b
    
    
def moving(x,y): # 그 점의 좌표로 이동하기 up(), goto(), down()사용
    up()
    goto(x,y)
    down()

def polygon(): # 도형의 종류와 한변의 길이를 입력받아 도형 그리기
    n,a = map(int, input("형의 종류(3이상) 한변의 길이(5이상)").split())
    for i in range(n):
        forward(10*a)
        left(360/n)
    
    
print("===도형만들기===")
while True:
    moving(*input_data())
    polygon()
    con = int(input("계속할래요?(1) 안할래요?(아무거나)"))
    if con != 1:
        break