# Draw a Smiley Face
import turtle

# Set up the turtle
t = turtle.Screen()
t.bgcolor("white")

#  for drawing face
face = turtle.Turtle()
face.penup()
face.goto(0, -100)
face.pendown()
face.color("yellow")
face.begin_fill()
face.circle(100)
face.end_fill()

# For the left eye
eye1=turtle.Turtle()
eye1.penup()
eye1.goto(-35,30)
eye1.pendown()
eye1.color("black")
eye1.begin_fill()
eye1.circle(10)
eye1.end_fill()

# For the right eye
eye2=turtle.Turtle()
eye2.penup()
eye2.goto(35,30)
eye2.pendown()
eye2.color("black")
eye2.begin_fill()
eye2.circle(10)
eye2.end_fill()

# For the smile
smile = turtle.Turtle()
smile.penup()
smile.goto(-40, -20)
smile.setheading(-60)
smile.pendown()
smile.circle(50, 120)

# Hide the turtles
face.hideturtle()
eye1.hideturtle()
eye2.hideturtle()
smile.hideturtle()

#Finish up
turtle.done()