from turtle import *

tracer(0)
lt(90)
m = 10
for i in range(9):
    fd(17 * m)
    lt(90)
    fd(8 * m)
    lt(90)
    fd(17 * m)
up()
lt(90)
fd(3 * m)
rt(90)
fd(5 * m)
lt(90)
down()
for i in range(4):
    fd(97 * m)
    rt(90)
    fd(132 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "white")
update()
done()
