from turtle import *

tracer(0)
lt(90)
m = 15
for i in range(4):
    fd(m * 16)
    lt(90)
    fd(m * 20)
    lt(90)
up()
fd(4 * m)
lt(90)
fd(8 * m)
rt(180)
down()
for i in range(3):
    fd(35 * m)
    lt(90)
    fd(6 * m)
    lt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(m * x, m * y)
        dot(3, "white")

done()
