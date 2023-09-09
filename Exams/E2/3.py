def dfs(current, previous, flowers, count, graph, f, end):
    if flowers > f:
        return 0
    elif current == end:
        return 1
    for city in graph[current]:
        if city != previous:
            return dfs(city, current, graph[city][current], count, graph, f, end)

n = int(input())
graph = [{} for _ in range(n)]
edges = []
for _ in range(n - 1):
    u, v, f = map(int, input().split())
    graph[v-1][u-1] = f
    graph[u-1][v-1] = f
    edges.append((v-1, u-1, f))

start = graph[0].keys() 
for u, v, f in edges:
    count = 0
    for start in range(n):
        for end in range(n):
            if start != end:
                count += dfs(start, None, 0, count, graph, f, end)
    print(count, end=' ')


