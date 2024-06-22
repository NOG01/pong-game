import turtle

sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("black")
sc.setup(width=1920, height=1080)

left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6,stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6,stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("red")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx=5
hit_ball.dy=-5

left_player = 0
right_player = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("red")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0 Right_player: 0",
             align="center", font=("Courier",
                                   24, "normal"))

def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)
def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)
def paddlebup():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)
def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)

sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
