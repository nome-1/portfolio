import turtle

window = turtle.Screen()
window.title("Helping Hand")
window.bgcolor('blue')
window.setup(width=800, height=600)
window.tracer(0)
pointsA = 0
pointsB = 0
# todo paddle a
padA = turtle.Turtle()
padA.speed(0)
padA.shape('square')
padA.color('white')
padA.shapesize(stretch_wid=5, stretch_len=1)
padA.penup()
padA.goto(-350, 0)
# todo paddle b
padb = turtle.Turtle()
padb.speed(0)
padb.shape('square')
padb.color('white')
padb.shapesize(stretch_wid=5, stretch_len=1)
padb.penup()
padb.goto(350, 0)
# todo ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape('square')
Ball.color('white')
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.5
Ball.dy = 0.5
# todo Pen
pen = turtle.Turtle()
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# todo function
def padA_up():
    y = padA.ycor()
    y += 20
    padA.sety(y)


def padA_down():
    y = padA.ycor()
    y -= 20
    padA.sety(y)


def padb_up():
    y1 = padb.ycor()
    y1 += 20
    padb.sety(y1)


def padb_down():
    y1 = padb.ycor()
    y1 -= 20
    padb.sety(y1)


# Keyboard binding
window.listen()
window.onkeypress(padA_up, "w" or "W")
window.onkeypress(padA_down, "s" or "S")
window.onkeypress(padb_up, "Up")
window.onkeypress(padb_down, "Down")
# main game loop
inverse = -1
i = True
while i:
    window.update()

    # todo move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # todo border check
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        pointsA += 1
        pen.clear()
        pen.write('player A:{}  player B:{}'.format(pointsA, pointsB), align='center')
    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        pointsB += 1
        pen.clear()
        pen.write('player A:{}  player B:{}'.format(pointsA, pointsB), align='center')
    # todo paddle and ball collisions
    if 340 < Ball.xcor() < 350 and (padb.ycor() + 40 > Ball.ycor() > padb.ycor() - 40):
        Ball.setx(340)
        Ball.dx *= -1

    if -340 > Ball.xcor() < -350 and (padA.ycor() + 40 > Ball.ycor() > padA.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1
