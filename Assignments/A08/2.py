import math

def dfs(node, parent, depth, graph, heights, ancestors):
    heights[node] = depth
    ancestors[node][0] = parent

    for i in range(1, len(ancestors[node])):
        ancestors[node][i] = ancestors[ancestors[node][i-1]][i-1]

    for child in graph[node]:
        if child != parent:
            dfs(child, node, depth + 1, graph, heights, ancestors)

def find_lca(u, v, heights, ancestors):
    if heights[u] < heights[v]:
        u, v = v, u

    diff = heights[u] - heights[v]

    while diff > 0:
        i = int(math.log2(diff))
        u = ancestors[u][i]
        diff -= 1 << i

    if u == v:
        return u

    for i in range(len(ancestors[u]) - 1, -1, -1):
        if ancestors[u][i] != ancestors[v][i]:
            u = ancestors[u][i]
            v = ancestors[v][i]

    return ancestors[u][0]


n, q = map(int, input().split())
p = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    graph[p[i-1]].append(i+1)

heights = [0] * (n + 1)
ancestors = [[0] * int(math.log2(n)) for _ in range(n + 1)]
dfs(1, 0, 0, graph, heights, ancestors)


for _ in range(q):
    u, v = map(int, input().split())
    lca = find_lca(u, v, heights, ancestors)
    print(lca)
