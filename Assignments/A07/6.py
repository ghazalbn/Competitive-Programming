from queue import Queue

def find_furthest(i, adj):
    dist = [-1] * n
    dist[i] = 0
    q = Queue()
    q.put(i)

    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.put(v)
    return dist

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)
    
dist = find_furthest(0, adj)
v = dist.index(max(dist))
dist = find_furthest(v, adj)
print(max(dist))
