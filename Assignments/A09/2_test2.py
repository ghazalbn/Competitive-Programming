def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, i, j):
    i_root = find(parent, i)
    j_root = find(parent, j)
    if i_root == j_root:
        return
    if rank[i_root] < rank[j_root]:
        parent[i_root] = j_root
    elif rank[i_root] > rank[j_root]:
        parent[j_root] = i_root
    else:
        parent[j_root] = i_root
        rank[i_root] += 1

n, q = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0] * (n+1)
max_y = [i for i in range(n+1)]

for _ in range(q):
    op_type, x, y = map(int, input().split())
    if op_type == 1 and max_y[x] != y:
        union(parent, rank, x, y)
    elif op_type == 2:
        i = x
        while i < y:
            if max_y[i] > i:
                i = max_y[i]
            else:
                union(parent, rank, i, i+1)
                max_y[i] = max(max_y[i], y)
                i += 1
    elif op_type == 3:
        if find(parent, x) == find(parent, y):
            print("YES")
        else:
            print("NO")
