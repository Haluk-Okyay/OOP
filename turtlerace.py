from turtle import Turtle
from random import randint

oz = Turtle()
oz.color('navy')
oz.shape('turtle')

sha = Turtle()
sha.color("black")
sha.shape("turtle")

tim = Turtle()
tim.color("grey")
tim.shape("turtle")

chris = Turtle()
chris.color ("green")
chris.shape("turtle")

oz.penup()
oz.goto(-160, 100)
oz.pendown()

sha.penup()
sha.goto(-160,70)
sha.pendown()

tim.penup()
tim.goto(-160,40)
tim.pendown()

chris.penup()
chris.goto(-160, 10)
chris.pendown()


for move in range(100):
    sha.forward(randint(1,5))
    oz.forward(randint(1,5))
    tim.forward(randint(1,5))
    chris.forward(randint(1,5))

input("Press a key to close")
