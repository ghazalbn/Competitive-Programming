t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())

    vv = []
    pp = ppx = 0

    for i in range(n):
        v = sorted(map(int, input().split()))
        ans, s = 0, 0
        cumulative_sum = [0] * m

        for j in range(m):
            s += v[j]
            cumulative_sum[j] = s

            if s > h:
                break

        if j == m:
            j -= 1

        if s > h:
            j -= 1
            ans -= s

        vv.append((j, ans))

        if i == 0:
            pp = j
            ppx = ans

    vv.sort(key=lambda x: (-x[0], x[1]))

    final = 0
    for i, it in enumerate(vv):
        if it == (pp, ppx):
            final = i + 1
            break

    print(final)
