
import turtle
import time
import winsound


#sound

def play():
    winsound.PlaySound('touch.wav',winsound.SND_ASYNC)
def winner():
    winsound.PlaySound('win.wav',winsound.SND_ASYNC)


# creating a window
wn = turtle.Screen()
wn.title("Pong Game")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.bgpic("bgp.gif")

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-390, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(380, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)


# Score
score_a = 0
score_b = 0

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0 Player B : 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Key Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# Main game loop
while True:
    if score_a == 3 or score_b == 3:
        pen.clear()
        pen.goto(0, 0)
        if score_a > score_b:
            pen.write("Player A wins!", align="center", font=("Courier", 50, "bold"))
            winner()
        else:
            pen.write("Player B wins!", align="center", font=("Courier", 50, "bold"))
            winner()
        time.sleep(5)
        break
    wn.update()
    # Moving the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.setx(390)
        ball.dx *= -1
    elif ball.xcor() < -392:
        score_b += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.setx(-390)
        ball.dx *= -1
    # Paddle & Ball Collisions
    if ball.xcor() > 380 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        play()
    elif ball.xcor() < -390 and paddle_b.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        play()