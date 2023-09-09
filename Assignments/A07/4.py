def bfs(edges, x):
    visited = [False] * n
    stack = [x]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(edges[node])

    for v in range(n):
        if len(edges[v]) > 0 and not visited[v]:
            return False
    return True

n, m = map(int, input().split())

edges = [[] for _ in range(n)]
degree = [0] * n
for _ in range(m):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
    degree[u-1] += 1
    degree[v-1] += 1

hamband = True
for v in range(n):
    if len(edges[v]) > 0:
        hamband = bfs(edges, v)
        break

count = sum(1 for d in degree if d % 2 == 1)
print("YES" if count in [0, 2] and hamband else "NO")

