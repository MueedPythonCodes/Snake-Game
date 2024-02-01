from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_body = []
        self.make_snake()
        self.head = self.turtle_body[0]

    def make_snake(self):
        for i in POSITION:
            self.add_segment(i)

    def add_segment(self, i):
        tur = Turtle(shape="square")
        tur.color("white")
        tur.penup()
        tur.goto(i)
        self.turtle_body.append(tur)

    def reset_snake(self):
        for snake in self.turtle_body:
            snake.goto(1000, 1000)
        self.turtle_body.clear()
        self.make_snake()
        self.head = self.turtle_body[0]

    def extend_snake(self):
        self.add_segment(self.turtle_body[-1].position())

    def move(self):
        for box in range(len(self.turtle_body)-1, 0, -1):
            x_axis = self.turtle_body[box-1].xcor()
            y_axis = self.turtle_body[box-1].ycor()
            self.turtle_body[box].goto(x=x_axis, y=y_axis)

        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)




















# from turtle import Turtle
#
# screen = Screen()
# screen.bgcolor("black")
#
# position = [(0, 0), (-20, 0), (-40, 0)]
# turtle_body = []
#
#
# def Snake():
#     for i in range(0, 3):
#         turtle = Turtle(shape="square")
#         turtle.color("white")
#         turtle.penup()
#         turtle.goto(position[i])
#         turtle_body.append(turtle)
#
#
# def move_snake():
#     for box in range(len(turtle_body)-1, 0, -1):
#         x_axis = turtle_body[box-1].xcor()
#         y_axis = turtle_body[box-1].xcor()
#         turtle_body[box].goto(x=x_axis, y=y_axis)
#
#
# if __name__ == "__main__":
#     snake()
#
#
# screen.exitonclick(
