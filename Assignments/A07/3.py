n, m = map(int, input().split())
edges = [set() for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u-1].add(v-1)
    edges[v-1].add(u-1)

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    if v-1 in edges[u-1]:
        print("NO")
    else:
        print("YES")
