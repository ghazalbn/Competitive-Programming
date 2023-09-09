t = int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_max = [0] * (2*n+1)
    b_max = [0] * (2*n+1)
    num = 0
    for i, ai in enumerate(a):
        num = 1 if ai != a[i-1] else num + 1
        a_max[ai] = max(num, a_max[ai])

    num = 0
    for i, bi in enumerate(b):
        num = 1 if bi != b[i-1] else num + 1
        b_max[bi] = max(num, b_max[bi])

    max_length = max(a_max[i] + b_max[i] for i in range(1, 2 * n + 1))
    print(max_length)