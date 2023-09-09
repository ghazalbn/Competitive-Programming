def dfs(adj, node, d):
    stack = [node]
    d[node] = 0
    visited = [False] * n
    while stack:
        c = stack.pop() 
        visited[c] = True
        for v in adj[c]:
            if not visited[v]:
                d[v] = d[c] + 1
                stack.append(v)

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

d1, d2 = [0] * n, [0] * n
dfs(adj, 0, d1)
dfs(adj, d1.index(max(d1)), d1)
dfs(adj, d1.index(max(d1)), d2)

for i in range(n):
    d2[i] = max(d2[i], d1[i])

d2.sort()
ans = 0
for k in range(1,n+1):
    while ans < n and d2[ans] < k:
        ans+=1
    
    print(min(n,ans+1),end=" ")


		  					   	  	  	   			 	   	