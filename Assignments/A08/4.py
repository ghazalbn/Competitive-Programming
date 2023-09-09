from collections import defaultdict, deque

def bfs(node, graph, s):
    visited = set()
    queue = deque()
    queue.append(node)
    visited.add(node)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return s in visited

def dfs(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

def count_teleport_pipes(n, m, graph):
    max_removed_edges = 0

    for node in range(1, n+1):
        i = 0
        while i < len(graph[node]):
            neighbor = graph[node][i]
            graph[node].remove(neighbor) 
            # if bfs(node, graph, neighbor):
            visited = set()
            dfs(node, graph, visited)
            if neighbor in visited:
                max_removed_edges += 1
            else:
                graph[node].insert(i, neighbor)
                i += 1

    min_pipes = m - max_removed_edges
    return min_pipes


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    ai, bi = map(int, input().split())
    graph[ai].append(bi)

print(count_teleport_pipes(n, m, graph))
