N = 200005
MAX = 26

ans = [''] * N
x = [0] * MAX
c = [0] * MAX

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    res = "YES"

    x = list(map(int, input().split()))
    c = list(map(int, input().split()))

    for i in range(k):
        if c[i] > x[i]:
            res = "NO"
        if i > 0 and x[i] - x[i - 1] < c[i] - c[i - 1]:
            res = "NO"
    if res == "NO":
        print("NO")
        continue

    ans = ['a'] * n
    cur = 3
    ch = 'd'
    for i in range(k):
        for j in range(x[i] - 1, x[i] - 1 - (c[i] - cur - 1), -1):
            ans[j] = ch
        ch = chr(ord(ch) + 1)
        cur = c[i]

    print("YES")
    ch = 'a'
    for i in range(n):
        if ans[i] == 'a':
            print(ch, end="")
            ch = chr(ord(ch) + 1)
            if ch == 'd':
                ch = 'a'
        else:
            print(ans[i], end="")
    print()
