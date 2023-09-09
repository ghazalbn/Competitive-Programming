def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(sourse, dest):
    sourse_parent = find(sourse)
    dest_parent = find(dest)
    parent[dest_parent] = sourse_parent

def kruskal(v, edges):
    mst = []
    edges.sort(key=lambda x: x[2])
    for u in range(1, v + 1):
        parent[u] = u
    for u1, u2, w in edges:
        if find(u1) != find(u2):
            union(u2, u1)
            mst.append((u1, u2, w))
    return mst

def find_second_lowest_cost(v, mst, edges):
    second = float('inf')
    for e in mst:
        for u in range(1, v + 1):
            parent[u] = u
        v_num = 0
        s = 0
        for edge in edges:
            u1, u2, w = edge
            if e != edge and find(u1) != find(u2):
                s += w
                union(u2, u1)
                v_num += 1
        if v_num == v - 1 and s < second:
           second = s
    return second

v, e = map(int, input().split())

edges = []
parent = [0] * (e + 2)
for _ in range(e):
    u1, u2, w = map(int, input().split())
    edges.append((u1, u2, w))

mst = kruskal(v, edges)
second = find_second_lowest_cost(v, mst, edges)
print("-1" if second == float('inf') else second)
