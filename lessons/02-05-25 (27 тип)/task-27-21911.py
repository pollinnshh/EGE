from math import dist


def centroid(cluster):
    distance = []
    for dot in cluster:
        cnt = 0
        for dot2 in cluster:
            cnt += dist(dot, dot2)
        distance.append([cnt, dot])
    return min(distance)[1]


with open("27_A_21911.txt") as file:
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
    clusters.append(cluster)
print([len(cluster) for cluster in clusters])

center1 = centroid(clusters[0])
center2 = centroid(clusters[1])

ans_1 = (center1[0] + center2[0]) / 2
ans_2 = (center1[1] + center2[1]) / 2

print(int(ans_1 * 10_000), int(ans_2 * 10_000))

