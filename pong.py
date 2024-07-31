import turtle
turtle.Turtle()
wn=turtle.Screen()
wn.title("pong game")
wn.bgcolor("white")
wn.tracer(0)


def paddle_a():
    paddle_a=turtle.Turtle()
    paddle_a.penup()      #so it doesn't trace the drawing of the square
    paddle_a.shape("square")
    paddle_a.goto(-350,0)
    paddle_a.color("blue")
    paddle_a.shapesize(stretch_len=1,stretch_wid=5)
    paddle_a.speed(0)

def paddle_b():
    paddle_b=turtle.Turtle()
    paddle_b.penup()      #so it doesn't trace the drawing of the square
    paddle_b.shape("square")
    paddle_b.goto(350,0)
    paddle_b.color("red")
    paddle_b.shapesize(stretch_len=1,stretch_wid=5)
    paddle_b.speed(0)

def ball():
    ball=turtle.Turtle()
    ball.penup()      #so it doesn't trace the drawing of the square
    ball.shape("circle")
    ball.goto(0,0)
    ball.color("black")
    ball.speed(0)

def paddle_a_up():
    y = paddle_a.ycorr()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y =paddle_a.ycore()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_a.ycorr()
    y += 30
    paddle_a.sety(y)

def paddle_b_down():
    y =paddle_a.ycore()
    y -= 30
    paddle_a.sety(y)

wn.listen()
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

paddle_a()
paddle_b()
ball()

while True:
    wn.update()