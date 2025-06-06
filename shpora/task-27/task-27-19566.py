from math import dist


def centroid(cluster):
    dists = []
    for dot in cluster:
        cnt = 0
        for dot2 in cluster:
            cnt += dist(dot, dot2)
        dists.append([cnt, dot])
    return max(dists)[1]


# # a
# with open("27.17.A_19566.txt") as file:
#     data = [list(map(float, i.split())) for i in file]
#
# eps = 1
# clusters = []
# while data:
#     cluster = [data.pop()]
#     for dot in cluster:
#         for dot2 in data.copy():
#             if dist(dot, dot2) < eps:
#                 cluster.append(dot2)
#                 data.remove(dot2)
#     if len(cluster) > 10:
#         clusters.append(cluster)
#
# print([len(cluster) for cluster in clusters])
#
# centers = [centroid(cluster) for cluster in clusters]
# ans1 = sum(center[0] for center in centers) / len(centers)
# ans2 = sum(center[1] for center in centers) / len(centers)
# print(int(abs(ans1 * 10_000)), int(abs(ans2 * 10_000)))

# b
with open("27.17.B_19566.txt") as file:
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
    if len(cluster) > 10:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
ans1 = sum(center[0] for center in centers) / len(centers)
ans2 = sum(center[1] for center in centers) / len(centers)
print(int(abs(ans1 * 10_000)), int(abs(ans2 * 10_000)))
