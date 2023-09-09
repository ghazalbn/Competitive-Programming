def dfs(start, visited, graph):
    visited[start] = True
    for city in graph[start]:
        if not visited[city]:
            dfs(city, visited, graph)

n = int(input())
graph = [[] for _ in range(n)]
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[v-1].append(u-1)
    graph[u-1].append(v-1)
    edges.append((u-1, v-1))

# if n % 2 == 1:
#     print(-1)

count = 0
for i, edge in enumerate(edges):
    # edges.remove(edge)
    flag = 1
    u, v = edge
    graph[u].remove(v)
    graph[v].remove(u)
    for start in range(n):
        visited = [False] * n
        dfs(start, visited, graph)
        l = len([i for i in range(n) if visited[i]])
        if l % 2 == 1:
            # edges.insert(i, edge)
            graph[u].append(v)
            graph[v].append(u)
            flag = 0
            break
    count += flag

print(count if count > 0 else -1)




