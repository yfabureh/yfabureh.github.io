# Building a Pong

import turtle
import time

wn = turtle.Screen()
wn.title('Pong by Yusuf')
wn.bgcolor('black')
wn.bgpic('background.gif')
wn.setup(width=800, height=600)
wn.tracer(0) # it stops the window from updating.

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() # makes sure moving object does not draw anything on the window.
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Function
# Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y > 250:
        paddle_a.sety(250)
    else:
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    if y < -250:
        paddle_a.sety(-250)
    else:
        paddle_a.sety(y)

# Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y > 250:
        paddle_b.sety(250)
    else:
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    if y < -250:
        paddle_b.sety(-250)
    else:
        paddle_b.sety(y)

# Keyboard Binding
wn.listen() # Tells it to listen to keyboard input
wn.onkeypress(paddle_a_up, "w") #configures w as up button for paddleA
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'o')
wn.onkeypress(paddle_b_down, 'k')


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.5 # every time the ball moves it moves by two pixels, x moves 2
ball.dy = 0.5 # every time the ball moves it moves by two pixels, y moves 2

# Pen - For Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Arial', 24, 'normal'))


# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking

    # y borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # x borders
    if ball.xcor() > 349:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear() # prevents previous scores from overlapping
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Arial', 24, 'normal'))

    if ball.xcor() < -349:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear() # prevents previous scores from overlapping
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Arial', 24, 'normal'))

    # Paddle and Ball Collisions
    # Ball & Paddle B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50):
        ball.dx *= -1

    # Ball & Paddle A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1

    # If Player A Wins
    if score_a == 5 and score_a > score_b:
        pen.clear()  # prevents previous scores from overlapping
        pen.write(f'Player A Wins!', align='center', font=('Arial', 24, 'normal'))
        ball.goto(0, 0)
        time.sleep(4)
        score_a = 0
        score_b = 0
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Arial', 24, 'normal'))
        exit()

    # If Player B Wins
    if score_b == 5 and score_b > score_a:
        pen.clear()  # prevents previous scores from overlapping
        pen.write(f'Player B Wins!', align='center', font=('Arial', 24, 'normal'))
        ball.goto(0, 0)
        time.sleep(4)
        score_a = 0
        score_b = 0
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Arial', 24, 'normal'))
        exit()
