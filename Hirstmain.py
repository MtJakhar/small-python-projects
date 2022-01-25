import random
import turtle

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(199, 175, 117), (125, 36, 24), (169, 104, 56), (187, 158, 51), (207, 220, 211), (6, 56, 83), (222, 224, 228), (109, 67, 85), (40, 35, 34), (87, 141, 57), (20, 122, 175), (110, 160, 175), (75, 39, 48), (9, 67, 47), (64, 153, 137), (183, 98, 80), (133, 40, 43), (179, 201, 187), (208, 200, 125), (150, 176, 164), (178, 167, 170), (95, 141, 154), (31, 78, 59)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

turtle.Screen().exitonclick()


