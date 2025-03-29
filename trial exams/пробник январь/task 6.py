from turtle import *
tracer(0)
m = 10
lt(90)
for i in range(2):
    fd(5 * m)
    lt(90)
    bk(13 * m)
    lt(90)
up()
bk(10 * m)
rt(90)
fd(9 * m)
lt(90)
down()
for i in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30,30):
        goto(x * m, y * m)
        dot(3,"darkred")
