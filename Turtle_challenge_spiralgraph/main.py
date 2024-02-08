# from turtle import Turtle
#
# tim = Turtle()
# Tom = Turtle()
# terry = Turtle()

import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

# random_walk using (r, g, b) tuple:
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# colors = ["cyan", "deep sky blue", "lime", "orange red", "gold", "crimson", "blanched almond", "deep pink"]
# Draw shapes
# def draw_shape(num_sides):
#     angles = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angles)
#
# for shape_sides_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_sides_n)v


# random_walk
# direction = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")

# for _ in range(1000):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

def draw_spiralgraph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spiralgraph(5)



screen = t.Screen()
screen.exitonclick()
