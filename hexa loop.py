from polygons import *
from turtle import Turtle
t = Turtle()

def square(l):
    for i in range(6):
        t.forward(l)
        t.left(60)

def hexa(n,m):
    for j in range(n):
        square(m)
        t.left(360/n)


t.speed(100)
hexa(12,100)
t.hideturtle()
