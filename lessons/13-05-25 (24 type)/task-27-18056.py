from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        cnt = 0
        for dot2 in cluster:
            cnt += dist(dot, dot2)
        dists.append([cnt, dot])
    return min(dists)[1]

# 1
with open("27A_18056.txt") as file:
    cl1 = []
    cl2 = []
    for i in file:
        x, y = map(float, i.split())
        if x > 0.5 and y < -1:
            cl1.append((x, y))
        elif x < 0.5 and y > -1:
            cl2.append((x, y))

center1 = centroid(cl1)
center2 = centroid(cl2)

ans1 = (center1[0] + center2[0]) / 2
ans2 = (center1[1] + center2[1]) / 2
print(abs(int(ans1 * 100000)), abs(int(ans2 * 100000)))

# 2
with open("27B_18056.txt") as file:
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
    if len(cluster) > 10:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / len(clusters)
p_y = sum(center[1] for center in centers) / len(clusters)


print(abs(int(p_x * 100000)), abs(int(p_y * 100000)))