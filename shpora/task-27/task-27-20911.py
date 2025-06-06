from math import dist


def centroid(cluster):
    dists = []
    for dot in cluster:
        cnt = 0
        for dot2 in cluster:
            cnt += dist(dot, dot2)
        dists.append([cnt, dot])
    return min(dists)[1]


# a
with open("27_A_20911.txt") as file:
    cl1 = []
    cl2 = []
    for i in file:
        x, y = map(float, i.split())
        if y < 0:
            cl1.append((x, y))
        else:
            cl2.append((x, y))

center1 = centroid(cl1)
center2 = centroid(cl2)

ans1 = (center1[0] + center2[0]) / 2
ans2 = (center1[1] + center2[1]) / 2
print(int(ans1 * 10_000), int(ans2 * 10_000))

# b
with open("27_B_20911.txt") as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in file:
        x, y = map(float, i.split())
        if x > 6 and y > 6:
            cl1.append((x, y))
        elif -5 < y < 5 and x < 8:
            cl2.append((x, y))
        elif y < -8:
            cl3.append((x, y))

center1 = centroid(cl1)
center2 = centroid(cl2)
center3 = centroid(cl3)

ans1 = (center1[0] + center2[0] + center3[0]) / 3
ans2 = (center1[1] + center2[1] + center3[1]) / 3
print(int(ans1 * 10_000), int(ans2 * 10_000))
