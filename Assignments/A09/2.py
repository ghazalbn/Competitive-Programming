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

for _ in range(q):
    op_type, x, y = list(map(int, input().split()))
    if op_type == 1 and x!=y:
        union(parent, rank, x, y)
    elif op_type == 2:
        for i in range(x, y):
            union(parent, rank, i, i+1)
    elif op_type == 3:
        if find(parent, x) == find(parent, y):
            print("YES")
        else:
            print("NO")