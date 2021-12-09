from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

paused = False 

def is_paused():
    global paused
    if paused == True:
        paused = False
    else:
        paused = True 

def start_over():
    global game 
    game = True 
    snake_game()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(is_paused, ' ')
screen.onkey(start_over, 'c')
scoreboard.instructions()

game = True



#     screen.textinput(
#         'START OVER?', 'Would you like to start again? Press the "C" key and press OK.').lower()
def snake_game():
    
    global game
    while game:
        if not paused:
            screen.update()
            time.sleep(0.1)

            snake.move()
            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend()
                scoreboard.increase_score()

            if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 280 or snake.head.ycor() < -285:
                #game = False
                # scoreboard.game_over()
                scoreboard.reset()
                snake.reset()

            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    scoreboard.reset()
                    snake.reset()
                    #scoreboard.game_over()
                    #game = False
        else:
            screen.update()

snake_game()
screen.exitonclick()
