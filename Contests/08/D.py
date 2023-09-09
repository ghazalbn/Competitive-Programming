t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    diff = abs(a[0] - b[0])
    for i in range(1, n):
        diff = min(diff, abs(a[i] - b[i]), abs(a[i-1] - b[i-1]))
    print(diff)
