from turtle import Turtle

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DIS = 20
UP =90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.activate = False
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_seg = Turtle('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)    
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            x_cor = self.segments[seg_num -1].xcor()
            y_cor = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    # def pause(self):
    #     self.activate = True

    # def continue_(self):
    #     self.activate = True 

