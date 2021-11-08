# 画一个18*18的棋盘
import turtle

t = turtle.Pen()
t.speed(10)
for x in range(0, 19):
    t.penup()
    t.goto(-180, 180 - x * 20)
    t.pendown()
    t.forward(360)
for y in range(0, 19):
    t.penup()
    t.goto(-180 + y * 20, 180)
    t.pendown()
    t.goto(-180 + y * 20, -180)
turtle.done()

