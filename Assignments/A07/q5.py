def dfs(node, parent, d, dist):
    dist[node] = d
    for i in adj[node]:
        if i != parent:
            dfs(i, node, d+1, dist)

n = int(input())
adj = [[] for _ in range(n)]
dist1 = [0] * n
dist2 = [0] * n
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

dfs(0, 0, 0, dist1)

s = max(range(n), key=lambda x: dist1[x])
dfs(s, s, 0, dist1)

e = max(range(n), key=lambda x: dist1[x])
dfs(e, e, 0, dist2)

dist1 = sorted([max(dist1[i], dist2[i]) for i in range(n)])

ans = 0
for i in range(n):
    while ans < n - 1 and dist1[ans] <= i:
        ans += 1
    print(ans + 1, end=" ")
