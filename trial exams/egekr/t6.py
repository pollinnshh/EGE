from turtle import *

lt(90)
m = 10
tracer(0)
screensize(10000, 10000)
for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(14 * m)
rt(90)
fd(10 * m)
lt(90)
down()
for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 50):
        goto(x * m, y * m)
        dot(3, "red")

done()
