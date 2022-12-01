import turtle
from turtle import Screen
import time
from food import Food
from snake import Snake
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
turtle.tracer(0)

snake = Snake()
food = Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.body[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    if snake.body[0].xcor() > 300 or snake.body[0].xcor() < -300 or \
            snake.body[0].ycor() > 300 or snake.body[0].ycor() < -300:
        game_is_on = False

    for segment in snake.body[1:len(snake.body)]:
        if segment.distance(snake.body[0].xcor(), snake.body[0].ycor()) < 15:
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()
