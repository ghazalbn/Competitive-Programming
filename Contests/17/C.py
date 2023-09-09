# Read the number of test cases
t = int(input())

results = []

# Process each test case
for _ in range(t):
    n = int(input())
    edges = []
    adjacency_list = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    visited = [False] * (n + 1)
    readings = 0
    visit = 1
    visited[1] = True
    while visit < n:
        i = 0
        while i < len(edges):
            u, v = edges[i]
            if visited[u]:
                if not visited[v]:
                    visit += 1
                    visited[v] = True
                edges.remove((u, v))
            else:
                i += 1
        readings += 1

    print(readings)
            

