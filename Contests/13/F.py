t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    degrees = [0] * (n+1)
    
    for i in range(m):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
        
    central_vertex = degrees.index(max(degrees))
    x = degrees[central_vertex]
    y = len(set().union(*[edges[v] for v in edges[central_vertex]])) - x
    
    print(x, y)
