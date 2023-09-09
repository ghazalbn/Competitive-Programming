import math
t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    min_diff = abs(1 - p[0])
    for i in range(1, n):
        diff = abs(i + 1 - p[i])
        if diff != 0:
            min_diff = math.gcd(min_diff, diff)

    print(min_diff)
