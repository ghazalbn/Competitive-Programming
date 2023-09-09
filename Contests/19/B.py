q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    bad_count = 0
    for i in range(n):
        if a[i] % k != (i + 1) % k:
            bad_count += 1

    print("0" if bad_count == 0 else 1 if bad_count == 2 else -1)