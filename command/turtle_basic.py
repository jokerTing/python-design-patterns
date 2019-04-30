# -*- coding: utf-8 -*-
import turtle

turtle.setup(400, 400)
screen = turtle.Screen()
screen.title("Keyborad drwaing!")

t = turtle.Turtle()
distance = 10

def advance():
    t.forward(distance)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def retreat():
    t.backward(10)

def quit():
    screen.bye()

screen.onkey(advance, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(retreat, "s")
screen.onkey(quit, "Escape")

screen.listen()
screen.mainloop()
'''
# 线条蓝色 背景色红色
turtle.color('blue', 'red')
turtle.begin_fill()

for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.end_fill()
turtle.done()
'''