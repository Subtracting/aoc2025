import math

with open('input/day8_1.txt') as f:
    nodes = []
    for line in f.readlines():
        x, y, z = map(int, line.strip().split(","))
        nodes.append((x, y, z))

clusters = []
node_dist = []

for j in range(len(nodes) - 1):
    fnode = nodes[j]
    min_dist = 10**9
    min_pair = []
    for i in range(j + 1, len(nodes)):
        nnode = nodes[i]
        if fnode != nnode:
            dist = math.dist(fnode, nnode)
            min_pair = [fnode, nnode]
            node_dist.append((dist, min_pair))

for dist, min_pair in sorted(node_dist):
    cluster_idx = [k for k in range(len(clusters))
                   if min_pair[0] in clusters[k] or min_pair[1] in clusters[k]]
    if cluster_idx == []:
        clusters.append(set(min_pair))
    else:
        new_cluster = set(min_pair)
        for idx in cluster_idx:
            new_cluster.update(clusters[idx])
            clusters[idx] = set()
        clusters.append(new_cluster)
    if len(clusters[-1]) == len(nodes):
        wall_dist = min_pair[0][0] * min_pair[1][0]
        print(wall_dist)
        break
