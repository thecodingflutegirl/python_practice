from turtle import Turtle 

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(0,270)
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0,270)
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def instructions(self):
        self.goto(-290, -290)
        self.write('to pause = space', align='left', font=('Arial'
        , 18, 'normal'))
        self.goto(-290, -270)
        self.write('to continue = c', align='left', font=('Arial'
        , 18, 'normal'))
       