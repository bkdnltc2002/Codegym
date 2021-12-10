import turtle
color=("pink", "blue", "green", "yellow", "orange", "red")
turtle.bgcolor("black")

def drawelipse(rad):
    for i in range(2):
        turtle.circle(rad, 90)
        turtle.circle(rad // 2, 90)

def drawLoop():
    i=0
    while i<35:
        turtle.speed(10)
        turtle.pencolor(color[i % 6])
        drawelipse(100)
        turtle.rt(10)
        i+=1

drawLoop()
turtle.exitonclick()