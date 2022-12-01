import turtle

SNAKE_START_SIZE = 3
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for i in range(SNAKE_START_SIZE):
            t = turtle.Turtle(shape="square")
            t.color("white")
            t.penup()
            t.setx(-i * 20)
            self.body.append(t)

    def move(self):
        for i in range((len(self.body) - 1), 0, -1):
            self.body[i].goto(self.body[i - 1].xcor(), self.body[i - 1].ycor())
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if not self.body[0].heading() == 270:
            self.body[0].setheading(90)

    def down(self):
        if not self.body[0].heading() == 90:
            self.body[0].setheading(270)

    def left(self):
        if not self.body[0].heading() == 0:
            self.body[0].setheading(180)

    def right(self):
        if not self.body[0].heading() == 180:
            self.body[0].setheading(0)

    def grow(self):
        t = turtle.Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(self.body[-1].xcor(), self.body[-1].ycor())
        self.move()
        self.body.append(t)
