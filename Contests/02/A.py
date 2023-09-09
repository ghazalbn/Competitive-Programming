t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    result = [-1] * n
    member = [0] * (n + m)
    r, j = 1, n - 1

    for i in p:
        if j >= 0 and not member[i - 1]:
            result[j] = r
            member[i - 1] = 1
            j -= 1
        r += 1
        
    print(*result)
