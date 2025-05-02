from math import dist


def centroid(cluster):
    distance = []
    for dot in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot, dot2)
        distance.append([sumd, dot])
    return min(distance)[1]


# 1
with open("27_A_21932.txt") as file:
    data = [list(map(float, i.split())) for i in file]

eps = 1
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
print(int(centers[1][0] * 10_000), int(centers[0][1] * 10_000))

# 2
with open("27_B_21932.txt") as file:
    data = [list(map(float, i.split())) for i in file]

eps = 1
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
print(int(centers[2][0] * 10_000), int(centers[1][1] * 10_000))
