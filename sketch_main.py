from turtle import Turtle, Screen

tr = Turtle()
screen = Screen()


def move_forward():
    tr.forward(10)

def move_backward():
    tr.backward(10)

def turn_left():
    tr.left(10)

def turn_right():
    tr.right(10)

def clear():
    tr.clear()
    tr.penup()
    tr.home()
    tr.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
