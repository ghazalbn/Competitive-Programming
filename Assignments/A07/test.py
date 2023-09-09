def find(parents, i):
    if parents[i] == i:
        return i
    parents[i] = find(parents, parents[i])
    return parents[i]

def union(parents, i, j):
    pi, pj = find(parents, i), find(parents, j)
    parents[pi] = pj

def bfs(edges, x):
    parents = list(range(n))
    for u, v in enumerate(edges):
        union(parents, u, v)
    root = find(parents, x)
    return all(find(parents, i) == root for i in range(n))

n, m = map(int, input().split())

edges = [[] for _ in range(n)]
degree = [0] * n
count = 0
for _ in range(m):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
    degree[u-1] += 1
    degree[v-1] += 1
    if degree[u-1] % 2 == 1:
        count += 1
    if degree[v-1] % 2 == 1:
        count += 1

hamband = True
for v in range(n):
    if len(edges[v]) > 0 and not bfs(edges, v):
        hamband = False
        break

print("YES" if count in [0, 2] and hamband else "NO")
