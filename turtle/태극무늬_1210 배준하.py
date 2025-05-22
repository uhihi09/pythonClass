import turtle

t = turtle.Turtle()
t.shape("turtle")
turtle.hideturtle()
turtle.bgcolor("black")

t.speed(0)
for i in range(1000):
    if i%3 == 0:
        t.pencolor("yellow")
    elif i%3 == 1:
        t.pencolor("blue")
    elif i%3 == 2:
        t.pencolor("red")
    t.left(119)
    t.forward(i*2)

turtle.done()