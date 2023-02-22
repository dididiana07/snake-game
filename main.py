from snake import Snake
from turtle import Screen
from score import Score, game_over
from time import sleep
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
score = Score()

screen.listen()
screen.onkeypress(fun=snake.go_up, key="Up")
screen.onkeypress(fun=snake.go_down, key="Down")
screen.onkeypress(fun=snake.go_left, key="Left")
screen.onkeypress(fun=snake.go_right, key="Right")

food_obj = Food()
food_obj.change_position()

its_running = True


while True:
    head_x, head_y = snake.position_head()
    sleep(0.03)
    if its_running:
        snake.move()
        screen.update()
    if int(head_x) >= 330 or int(head_x) <= -340 or int(head_y) >= 320 or int(head_y) <= -310:
        its_running = False
        game_over()
        screen.exitonclick()
        quit()
    elif snake.head.distance(food_obj.get_position()[0], food_obj.get_position()[1]) <= 10:
        food_obj.change_position()
        score.add_score()
        snake.add_new_segment()
    for segment_distance in snake.get_segments_position():
        if snake.head.distance(segment_distance[0], segment_distance[1]) <= 10:
            its_running = False
            game_over()
            screen.exitonclick()
            quit()
    score.check_high_score()
