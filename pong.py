import turtle
turtle.Turtle()

def paddle_a():
    paddle_a=turtle.Turtle()
    paddle_a.penup()      #so it doesn't trace the drawing of the square
    paddle_a.shape("square")
    paddle_a.goto(0,-350)
    paddle_a.color("black")
    paddle_a.shapesize(stretch_len=50,stretch_wid=100)

def paddle_b():
    paddle_b=turtle.Turtle()
    paddle_b.penup()      #so it doesn't trace the drawing of the square
    paddle_b.shape("square")
    paddle_b.goto(0,350)
    paddle_b.color("black")
    paddle_b.shapesize(stretch_len=50,stretch_wid=100)

paddle_a
paddle_b