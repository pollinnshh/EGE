from turtle import *

tracer(0)
lt(90)
m = 18
screensize(10000,100000)
rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * m, y * m)
        dot(3, "red")

done()
