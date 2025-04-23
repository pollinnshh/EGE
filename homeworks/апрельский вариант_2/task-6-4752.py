from turtle import *

tracer(0)
m = 20
lt(90)
for i in range(15):
    fd(4 * m)
    rt(60)
up()
for x in range(1, 30):
    for y in range(1, 30):
        goto(x * m, y * m)
        dot(3, "red")

done()
