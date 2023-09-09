t = int(input())
while t > 0:
    n, m, h = map(int, input().split())
    two_arr = []
    pp, ppx = 0, 0
    for _ in range(n):
        v = list(map(int, input().split()))
        v.sort()
        answer, s = 0, 0
        j = 0
        for j in range(m):
            s += v[j]
            answer += s
            if s > h:
                break
        if j == m:
            j -= 1
            answer -= s
        two_arr.append((j, answer))
        if _ == 0:
            pp = j
            ppx = answer
    two_arr.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    final = 0
    for it in two_arr:
        final += 1
        if it[0] == pp and it[1] == ppx:
            break
    print(final)
