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
ball.dx=0.5
ball.dy=-0.5

#PEN
pen=turtle.Turtle()
pen.speed(0)
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: 0   playerB:0",align="center",font=("courior",24,"normal"))

# score
score_A=0
score_B=0

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

while True:
    wn.update()
    # ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    # boarder
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_A+=1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_A,score_B),align="center",font=("courior",24,"normal"))


    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_B+=1
        pen.clear()
        pen.write("player A: {}  player B: {}".format(score_A,score_B),align="center",font=("courior",24,"normal"))


        # paddle collision
    if ball.xcor()>340 and ball.xcor() <350 and ball.ycor()<paddle_B.ycor()+400 and ball.ycor()>paddle_B.ycor()-40:
        ball.setx(340)
        ball.dx*=-1

    if ball.xcor()<-340 and ball.xcor() >-350 and ball.ycor()<paddle_A.ycor()+400 and ball.ycor()>paddle_A.ycor()-40:
        ball.setx(-340)
        ball.dx*=-1