from turtle import *
import turtle 
clear()
win = turtle.Screen()
win.setup(700,500)

bgcolor('sky blue')
shape('turtle')
title("Happy New Year!!!")

up()
setpos(-140,200)
color('green')
fillcolor('green')
begin_fill()
x = y = 130
a, b, z = 40, 50, 80
for i in range(2):
    if i % 2 == 1:
        x += 100
        y, z = z, y
        a, b = b, a
    right(x)
    forward(z)
    left(x)
    forward(a)
    right(x)
    forward(100)
    left(x)
    forward(b)
    right(x)
    forward(y)
    left(x)
    if i % 2 == 0:
        forward(220)
end_fill()
fillcolor('yellow')
color('yellow')
setpos(-150,210)
begin_fill()
for i in range(5):
    forward(20)
    right(144)
end_fill()
color('green')

up()
goto(-150,-38)
fillcolor('orange')
color('orange')
begin_fill()
for i in range(2):
    forward(20)
    right(90)
    forward(60)
    right(90)
end_fill() 
goto(-140,-130)
write("Happy New Year!!!",align='center',font=("Verdana",20,'bold'))
p = [[-190,-98,'red'],[-120,-98,'blue']]
for i,j,k in p:
    goto(i,j)
    fillcolor(k)
    color(k)
    begin_fill()
    for i in range(2):
        forward(30)
        left(90)
        forward(30)
        left(90)
    end_fill()

a = [[70,140,-130,'white'],[50,140,-20,'white'],[30,140,65,'white'],
     [5,140,5,'black'],[5,140,25,'black'],[5,140,45,'black'],
     [5,130,95,'green'],[5,150,95,'green'],[3,130,97,'black'],
     [3,150,97,'black']]
for i,j,k,l in a:
    up()
    goto(j,k)
    color(l)
    begin_fill()
    circle(i)
    end_fill()
hideturtle()

down()
color('white')
goto(136,94)
b = [[230,30],[160,30]]
begin_fill()
color('orange')
for i,j in b:
    left(i)
    forward(j)
end_fill()

color('white')
down()
goto(100,45)
color('black')
width(5)
goto(70,0)

up()
color('sky blue')
goto(180,45)
down()
color('black')
goto(210,0)
width(5)