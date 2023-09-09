n, k = map(int, input().split())

for i in range(n):
    k -= int(input())

print("YES" if k <= 0 else "NO")
