# import colorgram

# colors = colorgram.extract('./images/hirst-severed-spots.jpg',30)

# rgb_list = []

# for color in colors :
#     rgb_list.append((color.rgb.r,color.rgb.g,color.rgb.b))

# print(rgb_list)

from turtle import Turtle, Screen
import random

chini = Turtle()
screen = Screen() 

screen.colormode(255)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

chini.penup()
chini.hideturtle()
chini.speed('fastest')
chini.setheading(225)
chini.forward(325)
chini.setheading(0)


for i in range(1, 101):    
    chini.dot(20,random.choice(color_list))
    chini.forward(50)
    if i % 10 == 0 :
        chini.left(90)
        chini.forward(50)
        chini.left(90)
        chini.forward(500)
        chini.right(180)     
       
    












screen.exitonclick()