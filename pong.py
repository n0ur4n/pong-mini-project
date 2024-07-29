import turtle
turtle.Turtle()

def paddle_a():
    paddle_a=turtle.Turtle()
    paddle_a.penup()      #so it doesn't trace the drawing of the square
    paddle_a.shape("square")
    paddle_a.goto(-350,0)
    paddle_a.color("black")
    paddle_a.shapesize(stretch_len=1,stretch_wid=5)
    paddle_a.speed(0)

def paddle_b():
    paddle_b=turtle.Turtle()
    paddle_b.penup()      #so it doesn't trace the drawing of the square
    paddle_b.shape("square")
    paddle_b.goto(350,0)
    paddle_b.color("black")
    paddle_b.shapesize(stretch_len=1,stretch_wid=5)
    paddle_b.speed(0)

def ball():
    ball=turtle.Turtle
    ball.penup()
    ball.shape("circle")
    ball.color("red")
    ball.shapesize(2)
    ball.speed(0)
    ball.goto(0,0)
paddle_a()
paddle_b()
ball()




def paddle_a_up():
    y = paddle_a.ycorr()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y =paddle_a.ycore()
    y -= 20


wn.listen()
wn.onkeypress(paddle_a_up,  "w")
wn.onkeypress(paddle_a_down,  "w")




