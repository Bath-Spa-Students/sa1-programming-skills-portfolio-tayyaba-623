# Turtle Graphis
import turtle
t = turtle.Turtle()
# Background color
turtle.bgcolor ("White")
colors = ["Blue" , "Dark blue"] 
# for loop
for x in range(400):
    t. forward (x + 1)
    t. right (89)
    t. pencolor (colors [x % 2])
turtle. done ()
