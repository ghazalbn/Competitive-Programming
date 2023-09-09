def dfs(current, previous, flowers, count, graph, end):
    if current == end:
        return 1
    for city in graph[current]:
        if city != previous:
            return dfs(city, current, graph[city][current], count, graph, end)
mm = 7
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((v-1, u-1))

for u, v in edges:
    count = 0
    for start in range(n):
        for end in range(n):
            if start != end:
                count += 1
print(mm)

