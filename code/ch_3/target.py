# target.py

import turtle

# Named constants

#Screen settigns
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# Targets Lower left Points
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
# Width of Target
TARGET_WIDTH = 25

FORCE_FACTOR = 30
PROJECTILE_SPEED = 1

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

t = turtle.Turtle()

# Window Setup
t.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Drawing Target
t.hideturtle()
t.speed(0)
t.penup()
t.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
t.pendown()
t.setheading(EAST)
t.forward(TARGET_WIDTH)
t.setheading(NORTH)
t.forward(TARGET_WIDTH)
t.setheading(WEST)
t.forward(TARGET_WIDTH)
t.setheading(SOUTH)
t.forward(TARGET_WIDTH)
t.penup()

# Centering the Turtle
t.goto(0,0)
t.setheading(EAST)
t.showturtle()
t.speed(PROJECTILE_SPEED)

# Getting input from user
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculating distance
distance = force * FORCE_FACTOR

# Set heading
t.setheading(angle)

# Launch projectile
t.pendown()
t.forward(distance)

# Did the turtle hit target?
if (t.xcor() >= TARGET_LLEFT_X and
    t.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    t.ycor() >= TARGET_LLEFT_Y and
    t.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("Target hit")
else:
    print("You missed the target.")
