import turtle as t
import random as rd

t.bgcolor('skyblue')

bin = t.Turtle()
t.register_shape('D:\\ash sjbit\\1JB22CD009 python miniproj\\gggarbage_bin.gif')
bin.shape('D:\\ash sjbit\\1JB22CD009 python miniproj\\gggarbage_bin.gif')
bin.color('black')
bin.speed(0)
#bin.penup()
bin.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('brown')
#leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False
text_turtle = t.Turtle()
text_turtle.write('              Welcome\nPress SPACE to trash IN bIN',align='center',font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = bin.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

def game_over():
    bin.color('skyblue')
    leaf.color('skyblue')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y)
    score_turtle.write('leaves collected\n\n', align = 'right',font=('Arial',10,'bold'))
    score_turtle.write(str(current_score)+'      ' , align = 'right',font=('Arial',25,'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    bin_speed = 2
    bin_length = 4
    bin.shapesize(1,bin_length,1)
    bin.showturtle()
    display_score(score)
    place_leaf()

    while True:
        bin.forward(bin_speed)
        if bin.distance(leaf)<20:
            place_leaf()
            bin_length = bin_length + 1
            bin.shapesize(1,bin_length,1)
            bin_speed = bin_speed + 1
            score = score + 1
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if bin.heading() == 0 or bin.heading() == 180:
        bin.setheading(90)

def move_down():
    if bin.heading() == 0 or bin.heading() == 180:
        bin.setheading(270)

def move_left():
    if bin.heading() == 90 or bin.heading() == 270:
        bin.setheading(180)

def move_right():
    if bin.heading() == 90 or bin.heading() == 270:
        bin.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()