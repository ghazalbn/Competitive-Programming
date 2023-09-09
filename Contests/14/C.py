N = 2e5 + 100

def preProc(s):
    vec = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            vec.append(i)
    vec.append(N)
    return vec

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input()
    vec = preProc(s)
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        ind = bisect.bisect_left(vec, l)
        if vec[ind] + 2 <= r:
            print("YES")
        else:
            print("NO")
