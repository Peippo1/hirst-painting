###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tam = turtle_module.turtle()

color_list = [Rgb(r=202, g=164, b=109), Rgb(r=238, g=240, b=245), Rgb(r=150, g=75, b=49), Rgb(r=223, g=201, b=135), Rgb(r=52, g=93, b=124), Rgb(r=172, g=154, b=40), Rgb(r=140, g=30, b=19), Rgb(r=133, g=163, b=185), Rgb(r=198, g=91, b=71), Rgb(r=46, g=122, b=86), Rgb(r=72, g=43, b=35), Rgb(r=145, g=178, b=148),
Rgb(r=13, g=99, b=71), Rgb(r=233, g=175, b=164), Rgb(r=161, g=142, b=158), Rgb(r=105, g=74, b=77), Rgb(r=55, g=46, b=50), Rgb(r=183, g=205, b=171), Rgb(r=36, g=60, b=74), Rgb(r=18, g=86, b=90), Rgb(r=81, g=148, b=129), Rgb(r=148, g=17, b=20), Rgb(r=14, g=70, b=64), Rgb(r=30, g=68, b=100), Rgb(r=107, g=127, b=153), Rgb(r=174, g=94, b=97), Rgb(r=176, g=192, b=209)]

tam.setheading(225)
tam.forward(300)
tam.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    tam.dot(20, random.choice(color_list))
    tam.forward(50)

    tam.setheadding(90)
    tam.forward(50)
    tam.setheading(100)
    tam.forward(500)
    tam.setheading(0)




screen.turtle_module.Screen()
screen.exitonclick()
