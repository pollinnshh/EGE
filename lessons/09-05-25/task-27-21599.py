from math import dist
import turtle

turtle.tracer(0)


def centroid(cluster):
    dists = []
    for dot in cluster:
        cnt = 0
        for dot2 in cluster:
            cnt += dist(dot, dot2)
        dists.append([cnt, dot])
    return min(dists)[1]


# 1
with open("27_A_21599.txt") as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in file:
        x, y = map(float, i.split())
        if y > 2 * x - 22:
            cl1.append([x, y])
        elif y < 2 * x - 22 and y > 0.25 * x - 9.75:
            cl2.append([x, y])
        elif y < 0.25 * x - 9.75:
            cl3.append([x, y])

center1 = centroid(cl1)
center2 = centroid(cl2)
center3 = centroid(cl3)

ans1 = (center1[0] + center2[0] + center3[0]) / 3
ans2 = (center1[1] + center2[1] + center3[1]) / 3
print(abs(int(ans1 * 10_000)), abs(int(ans2 * 10_000)))

clusters = []
clusters.append(cl1)
clusters.append(cl2)
clusters.append(cl3)

turtle.up()
colors = ["red", "purple", "darkblue"]
for cluster, color in zip(clusters, colors):
    for dot in cluster:
        turtle.goto(dot[0] * 8, dot[1] * 8)
        turtle.dot(3, color)

turtle.update()
turtle.done()

# 2
with open("27_B_21599.txt") as file:
    cl1 = []
    cl2 = []
    cl3 = []
    cl4 = []
    cl5 = []
    cl6 = []
    for i in file:
        x, y = map(float, i.split())
        if y < -2 * x - 26:
            cl1.append((x, y))
        elif y > -2 * x - 26 and x < - 10:
            cl2.append((x, y))
        elif y > 1.5 * x + 10.5 and x > - 10:
            cl3.append((x, y))
        elif y < 1.5 * x + 10.5 and y > 0.5 * x:
            cl4.append((x, y))
        elif y < 0.5 * x and y > -5:
            cl5.append((x, y))
        elif y < -5:
            cl6.append((x, y))

center1 = centroid(cl1)
center2 = centroid(cl2)
center3 = centroid(cl3)
center4 = centroid(cl4)
center5 = centroid(cl5)
center6 = centroid(cl6)

ans1 = (center1[0] + center2[0] + center3[0] + center4[0] + center5[0] + center6[0]) / 6
ans2 = (center1[1] + center2[1] + center3[1] + center4[1] + center5[1] + center6[1]) / 6
print(abs(int(ans1 * 10_000)), abs(int(ans2 * 10_000)))
