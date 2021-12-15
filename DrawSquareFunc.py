import turtle

pen = turtle.Turtle()
pen.speed(100)
pen.color(0, 0, 0)
wn = turtle.Screen()
wn.bgcolor("blue")


def drawDoor(pen, x, y):
    # door
    pen.penup()
    pen.goto(x, y)
    pen.fillcolor(180, 0, 0)
    pen.begin_fill()
    pen.setheading(90)

    for x in range(2):
        pen.forward(50)
        pen.right(90)
        pen.forward(30)
        pen.right(90)

    pen.end_fill()

    # handle
    pen.fillcolor("yellow")
    pen.penup()
    pen.goto(x, y + 20)
    pen.begin_fill()
    pen.circle(4)
    pen.end_fill()


def drawWindow(pen, x, y, shape):
    pen.width(4)
    pen.color("black")
    pen.fillcolor("lightblue")

    if shape == "square":
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.begin_fill()

        for y in range(4):
            for x in range(4):
                pen.forward(20)
                pen.right(90)
            pen.left(90)
        pen.end_fill()
    else:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.backward(20)
        pen.right(90)
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()
        pen.goto(x, y)

        for x in range(2):
            pen.forward(20)
            pen.backward(40)
            pen.forward(20)
            pen.right(90)


drawWindow(pen, -95, 15, "square")
drawHouse(pen)
drawDoor(pen, -25, -20)
drawBush(pen, 120, 35)
drawWindow(pen, -10, 100, "circle")
drawFence(pen)
drawPath(pen)
drawWindow(pen, -95, 100, "square")
drawGrass(pen)
drawCloud(pen, 75, 160)
drawWindow(pen, 75, 15, "square")
drawSun(pen, -200, 160, 70)
drawWindow(pen, 180, 150, "square")