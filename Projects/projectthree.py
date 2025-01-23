
import turtle

#Setup

t = turtle. Turtle()
t.penup()
t.goto(100,-100)
t.pendown()
t.speed(100)

#Background

t.color ( "light blue" )
for i in range(1000):
    t.forward(200 + i)
    t.right(90)

t.penup()
t.goto(150,-250)
t.pendown()

#Mountains

t.color ( "grey" )
for i in range (700):
    t.forward(10 +i)
    t.left(120)

t.penup()
t.goto(-200,-250)
t.pendown()

t.color ( "grey" )
for i in range (500):
    t.forward(10 +i)
    t.left(120)

#sun

t.penup()
t.goto(-200,100)
t.pendown()

t.color ( "yellow" )
for i in range(200):
    t.forward(5)
    t.left(5)

#Finish

turtle.exitonclick()