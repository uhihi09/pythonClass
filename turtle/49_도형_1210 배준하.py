import turtle

t = turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(-200,200)
t.down()
t.fillcolor("yellow")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.up()
t.goto(100,100)
t.down()
t.pencolor("red")
for i in range(3):
    t.forward(100)
    t.left(120)

turtle.done()