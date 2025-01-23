import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")

height = 50

# stripes

# move to stripe 1
t.penup
t.goto(-250, -100)
t.pendown

# stripe 1
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()


# move to stripe 2
t.penup
t.goto(-250, -50)
t.pendown

# stripe 2
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 3
t.penup
t.goto(-250, 0)
t.pendown

# stripe 3
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 4
t.penup
t.goto(-250, 50)
t.pendown

# stripe 4
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 5
t.penup
t.goto(-250, 100)
t.pendown

# stripe 5
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# blue square
t.penup
t.goto(-250,0)
t.pendown

t.color("blue")
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.end_fill()

#stars

turtle.exitonclick()
