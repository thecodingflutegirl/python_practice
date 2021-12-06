import turtle
import random

tim = turtle.Turtle()
tim.shape('arrow')
screen = turtle.Screen()

# to create a square
for _ in range(4):
    tim.right(90)
    tim.forward(100)

# to create a dashed line
for _ in range(12):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# to create triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon each with random color
# each side is 100
colors = ['red', 'blue', 'green', 'purple', 'pink',
          'orange', 'yellow', 'teal', 'lavendar', 'gray']


def draw(sides):
    angle = 360/sides
    for _ in range(sides):
        tim.right(angle)
        tim.forward(100)


for sides in range(3, 11):
    tim.color(random.choice(colors))
    draw(sides)

# generate a random walk
directions = [0, 90, 180, 270]
colors = ['red', 'blue', 'green', 'purple', 'pink',
         'orange', 'yellow', 'teal', 'gray']
tim.pensize(30)
tim.speed('fastest')

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


# create random color in turtle
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.color(random_color())

# Make a spirograph

tim.speed('fastest')
def spirograph(gap):
    for _ in range(int(360/gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + gap)
        tim.circle(100)
        tim.color(random_color())

spirograph(5)

# CREATING A MILLION DOLLAR PAINTING
# --- need to get colors wanted from colorgram below, the list of all the colors is below as color_list
#import colorgram
# colors = colorgram.extract('image.jpg', 20)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r , g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors) --- this list is what made up color_list 
color_list = [(9, 15, 56), (55, 5, 44), (157, 11, 119), (14, 111, 184), (8, 37, 16), (28, 30, 165), (41, 22, 7), (213, 18, 169), (234, 37, 173), (7, 171, 225),
              (142, 89, 31), (38, 127, 65), (43, 191, 102), (214, 237, 46), (161, 170, 26), (21, 95, 41), (80, 85, 13), (225, 155, 64), (71, 215, 111), (71, 245, 134)]


tim.hideturtle()
tim.penup()
tim.goto(-200, -200)
for _ in range(5):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    for _ in range(2):
        tim.left(90)
        tim.forward(50)

    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    for _ in range(2):
        tim.right(90)
        tim.forward(50)



###### ANGELA's SOLUTION for the million dollar painting 

tim.speed('fastest')
tim.penup()
# color_list
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dots = 100

for dot in range( 1, dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


        

screen.exitonclick()