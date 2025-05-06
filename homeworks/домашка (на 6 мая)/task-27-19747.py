from math import dist

def centroid(cluster):
    dstnce = []
    for dot in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot, dot2)
        dstnce.append([sumd, dot])
    return min(dstnce)[1]

# 1
with open("27A_19747.txt") as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.65
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

p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)

print(int(p_x * 10_000), int(p_y * 10_000))

# 2
with open("27B_19747.txt") as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.278
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

p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)

print(int(p_x * 10_000), int(p_y * 10_000))