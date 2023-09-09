n, m = map(int, input().split())
b = [0] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    b[u] = b[u] | 1 << v
    b[v] = b[v] | 1 << u

t = False
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if bin(b[i] & b[j]).count('1') > 2:
            t = True
            break
print("YES" if t else "NO")
