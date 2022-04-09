import random
import turtle
from turtle import Turtle,Screen

rat = Turtle()
time = Screen()
time.setup(width=300, height=450)
time.title("Love From Code_x")
turtle.colormode(255)

def col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pick = (r, g, b)
    return pick




rat.color(col())  # colling the col function

rat.begin_fill()
rat.pensize(3)
rat.left(50)
rat.forward(133)
rat.circle(50, 200)
rat.right(140)
rat.circle(50, 200)
rat.forward(133)
rat.end_fill()
time.exitonclick()
# tm.exit
# end_fill()

