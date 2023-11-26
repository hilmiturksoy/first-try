import turtle


my_screen=turtle.Screen()
my_screen.bgcolor("light blue")
my_screen.title("work")
turtle_instance=turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(10)
def turtle_right():
    turtle_instance.right(10)
def turtle_left():
    turtle_instance.left(10)
def turtle_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()
def turtle_clear():
    turtle_instance.clear()

def up():
    turtle_instance.penup()
def down():
    turtle_instance.pendown()




turtle.listen()
turtle.onkey(fun=turtle_forward,key="space")
turtle.onkey(fun=turtle_right,key="6")
turtle.onkey(fun=turtle_left,key="4")
turtle.onkey(fun=turtle_home,key="h")
turtle.onkey(fun=turtle_clear,key="c")
turtle.onkey(fun=up,key="0")
turtle.onkey(fun=down,key=",")



turtle.mainloop()