import turtle 
wn= turtle.Screen()
wn.title("pong game ")
wn.bgcolor("white")
wn.setup(width=800,height=600)
wn.tracer(0)

#paddle A
paddle_A=turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("blue")
paddle_A.shapesize(stretch_wid=5,stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350, 0)

#paddle_B
paddle_B=turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("red")
paddle_B.shapesize(stretch_wid=5,stretch_len=1)
paddle_B.penup()
paddle_B.goto(350, 0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)

def paddle_A_up():
    y=paddle_A.ycor()
    y+=20
    paddle_A.sety(y)
    
def paddle_A_down():
    y=paddle_A.ycor()
    y-=20
    paddle_A.sety(y)   

def paddle_B_up():
    y=paddle_B.ycor()
    y+=20
    paddle_B.sety(y)

def paddle_B_down():
    y=paddle_B.ycor()
    y-=20
    paddle_B.sety(y)

wn.listen()
wn.onkeypress(paddle_A_up, "w")
wn.onkeypress(paddle_A_down, "s")
wn.onkeypress(paddle_B_up, "Up")
wn.onkeypress(paddle_B_down, "Down")