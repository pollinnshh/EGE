from math import *


def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot, dot2)
        distance.append([sum_d, dot])
    return min(distance)[1]


# 1
with open("27_A_17916.txt") as file:
    cluster1 = []
    cluster2 = []
    for i in file:
        x, y = map(float, i.split())
        if y < 8:
            cluster1.append((x, y))
        else:
            cluster2.append((x, y))

center1 = centroid(cluster1)
center2 = centroid(cluster2)

ans1 = (center1[0] + center2[0]) / 2
ans2 = (center1[1] + center2[1]) / 2

print(int(ans1 * 10_000), int(ans2 * 10_000))
