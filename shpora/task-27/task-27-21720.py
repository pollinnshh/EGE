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
with open("27_A_21720.txt") as file:
    cl1 = []
    cl2 = []
    for i in file:
        x, y = map(float, i.split())
        if y < -1:
            cl1.append((x, y))
        else:
            cl2.append((x, y))

centr1 = centroid(cl1)
centr2 = centroid(cl2)

ans1 = (centr1[0] + centr2[0]) / 2
ans2 = (centr1[1] + centr2[1]) / 2
print(int(abs(ans1 * 10_000)), int(abs(ans2 * 10_000)))

# b
with open("27_B_21720.txt") as file:
    cl1 = []
    cl2 = []
    cl3 = []
    for i in file:
        x, y = map(float, i.split())
        if y > 8 and x < -6:
            cl1.append((x, y))
        elif 0 < y < 11 and x > -6:
            cl2.append((x, y))
        else:
            cl3.append((x, y))

centr1 = centroid(cl1)
centr2 = centroid(cl2)
centr3 = centroid(cl3)

ans1 = (centr1[0] + centr2[0] + centr3[0]) / 3
ans2 = (centr1[1] + centr2[1] + centr3[1]) / 3
print(int(abs(ans1 * 10_000)), int(abs(ans2 * 10_000)))
