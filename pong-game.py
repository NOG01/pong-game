import turtle

def start_game():
    global game_started
    game_started = True
    start_button.clear()
    start_button.hideturtle()
    draw_game_screen()

def draw_game_screen():
    sc = turtle.Screen()
    sc.title("Pong Game")
    sc.bgcolor("black")
    sc.setup(width=1280, height=720)

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
    hit_ball.dx=7
    hit_ball.dy=-7

    left_player = 0
    right_player = 0

    sketch = turtle.Turtle()
    sketch.speed(0)
    sketch.color("white")
    sketch.penup()
    sketch.hideturtle()
    sketch.goto(0, 260)
    sketch.write("Player One : 0 Player Two: 0",
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
    sc.onkeypress(paddleaup, "w")
    sc.onkeypress(paddleadown, "s")
    sc.onkeypress(paddlebup, "Up")
    sc.onkeypress(paddlebdown, "Down")

    while True:
        sc.update()
        hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
        hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

        if hit_ball.ycor() > 280:
            hit_ball.sety(280)
            hit_ball.dy *= -1
        if hit_ball.ycor() < -280:
            hit_ball.sety(-280)
            hit_ball.dy *= -1

        if hit_ball.xcor() > 500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1

        sketch.clear()
        sketch.write("Player One : {} Player Two : {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

        if hit_ball.xcor() < -500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            right_player += 1
            sketch.clear()
            sketch.write("Player One : {} Player Two: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

        if (hit_ball.xcor() > 360 and
                            hit_ball.xcor() < 370) and (hit_ball.ycor()
                                                        <right_pad.ycor()+40 and
                                                        hit_ball.ycor() > right_pad.ycor()-40):
                            hit_ball.setx(360)
                            hit_ball.dx*=-1

        if (hit_ball.xcor() < -360 and
                            hit_ball.xcor()>-370) and (hit_ball.ycor()
                                                       <left_pad.ycor()+40 and
                                                       hit_ball.ycor() > left_pad.ycor()-40):
                            hit_ball.setx(-360)
                            hit_ball.dx*=-1

sc = turtle.Screen()
sc.title("Pong Game Menu")
sc.bgcolor("black")
sc.setup(width=1280, height=720)

start_button = turtle.Turtle()
start_button.speed(0)
start_button.shape("square")
start_button.color("white")
start_button.penup()
start_button.goto(0, 0)
start_button.shapesize(stretch_wid=3, stretch_len=6)

start_button.write("Start Game", align="center", font=("Courier", 24, "normal"))

game_started = False

def check_click(x, y):
    if -60 < x < 60 and -30 < y < 30 and not game_started:
        start_game()

sc.onscreenclick(check_click)

turtle.done()
