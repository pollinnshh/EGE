from turtle import *

tracer(0)
m = 18
lt(90)
up()
screensize(10000, 10000)
for i in range(10):
    rt(120)
    fd(10 * m)
down()
for i in range(7):
    fd(15 * m)
    rt(90)
for i in range(5):
    rt(60)
    fd(20 * m)
    rt(30)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, 'darkred')
done()
