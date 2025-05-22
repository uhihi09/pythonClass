import turtle

t = turtle.Turtle()
t.shape("turtle")

# t.fillcolor("red")
# t.begin_fill(   )
t.pencolor("green")
for i in range(4):
    t.forward(100)
    t.left(90)
# t.end_fill()
t.pencolor("red")
t.circle(50)

t.pencolor("blue")
for i in range(3):
    t.forward(100)
    t.left(120)
turtle.done()