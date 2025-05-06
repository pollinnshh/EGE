from math import dist
import turtle

turtle.tracer(0)


def centroid(cluster):
    distn = []
    for dot in cluster:
        cnt = 0
        for dot2 in cluster:
            cnt += dist(dot, dot2)
        distn.append([cnt, dot])
    return max(distn)[1]


# 1
with open("27.19.A_20497.txt") as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.5
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 5:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)
print(int(p_x * 10_000), int(p_y * 10_000))

turtle.up()
colors = ["red", "purple", "darkblue"]
for cluster, color in zip(clusters, colors):
    for dot in cluster:
        turtle.goto(dot[0] * 40, dot[1] * 40)
        turtle.dot(3, color)

turtle.update()
turtle.done()

# 1 (2 способ)
with open("27.19.A_20497.txt") as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 0 and y < 0:
            cl1.append((x, y))
        elif 0 < y < 6 and x > -1:
            cl2.append((x, y))
        elif x > 0.5 and -6 < y < 0:
            cl3.append((x, y))

center1 = centroid(cl1)
center2 = centroid(cl2)
center3 = centroid(cl3)

ans1 = (center1[0] + center2[0] + center3[0]) / 3
ans2 = (center1[1] + center2[1] + center3[1]) / 3
print(int(ans1 * 10_000), int(ans2 * 10_000))

# 2
with open("27.19.B_20497.txt") as file:
    data = [list(map(float, i.split())) for i in file]

eps = 2
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)
print(int(p_x * 10_000), int(p_y * 10_000))
