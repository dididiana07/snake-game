import random
import turtle


class Food:
    def __init__(self):
        self.food = turtle.Turtle(shape="circle")
        self.food.shapesize(0.75)
        self.food.penup()
        self.food.color("pink")

    def change_position(self):
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        self.food.setpos(x, y)

    def get_position(self):
        return self.food.xcor(), self.food.ycor()
