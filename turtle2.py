from turtle import Turtle
from random import randint

ozan = Turtle()
eiko = Turtle()
masafumi = Turtle()
hidetoshi = Turtle()

ozan.color('blue')
ozan.shape('turtle')

ozan.penup()
ozan.goto(-160, 100)
ozan.pendown()

eiko.color('pink')
eiko.shape('turtle')

eiko.penup()
eiko.goto(-160, 130)
eiko.pendown()

masafumi.color('yellow')
masafumi.shape('turtle')
masafumi.penup()
masafumi.goto(-160, 70)
masafumi.pendown()

hidetoshi.color('black')
hidetoshi.shape('classic')
hidetoshi.penup()
hidetoshi.goto(-160, 40)
hidetoshi.pendown()

for movement in range(200):
    eiko.forward(randint(1,10))
    ozan.forward(randint(1,10))
    hidetoshi.forward(randint(1,10))
    masafumi.forward(randint(1,10))


