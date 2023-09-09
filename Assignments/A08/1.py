from collections import namedtuple  

import sys 
sys.setrecursionlimit(10**6)
  
vertex = namedtuple('vertex',['visited','neighbors'])


def dfs(adj, x, order):
    adj[x] = vertex(1, adj[x].neighbors)
    for n in adj[x].neighbors:
        if adj[n].visited == 0:
            dfs(adj, n, order)
    order.append(x)

def toposort(adj):
    order = []
    for i in range(len(adj)):
        if adj[i].visited == 0:
            dfs(adj, i, order)
    order.reverse()
    return order


n, m = map(int, input().split())
adj = [vertex(0, []) for _ in range(n)]
reverse_adj = [vertex(0, []) for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].neighbors.append(b - 1)
    reverse_adj[b - 1].neighbors.append(a - 1)
   
result = 0
order = toposort(reverse_adj)
adj = [vertex(0, adj[i].neighbors) for i in range(n)]
for i in order:
    if not adj[i].visited:
        tmp = []
        dfs(adj, i, tmp)
        result += 1
print(result)