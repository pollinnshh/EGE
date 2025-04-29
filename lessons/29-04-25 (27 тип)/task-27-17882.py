from math import dist


def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]


# 1
with open("27_A_17882.txt") as file:
    cluster1 = []
    cluster2 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 1:
            cluster1.append((x, y))
        else:
            cluster2.append((x, y))

center1 = centroid(cluster1)
center2 = centroid(cluster2)

ans_x = (center1[0] + center2[0]) / 2
ans_y = (center1[1] + center2[1]) / 2

print(int(ans_x * 10_000), int(ans_y * 10_000))

# 2
with  open("27_B_17882.txt") as file:
    clust1 = []
    clust2 = []
    clust3 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 3 and y < 4:
            clust1.append((x, y))
        elif x > 5:
            clust2.append((x, y))
        else:
            clust3.append((x, y))

cent1 = centroid(clust1)
cent2 = centroid(clust2)
cent3 = centroid(clust3)

ans_x = (cent1[0] + cent2[0] + cent3[0]) / 3
ans_y = (cent1[1] + cent2[1] + cent3[1]) / 3

print(int(ans_x * 10_000), int(ans_y * 10_000))
