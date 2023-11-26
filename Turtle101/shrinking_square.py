import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("yellow")
turtle_screen.title("shrinking")

pen = turtle.Turtle()
pen.color("blue")
pen.speed(15)


def shrink(size):
    for i in range(4):
        pen.forward(size)
        pen.left(90)
        size=size-5

shrink(200)
shrink(180)
shrink(160)
shrink(140)
shrink(120)
shrink(100)
shrink(80)
shrink(60)
shrink(40)
shrink(20)
shrink(10)

turtle.done()