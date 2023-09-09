import sys
sys.setrecursionlimit(10**7)
def check(n, m):
    if n == m:
        return "YES"
    for i in range(1, (n // 2) + 1):
        if n == i + (i * 2):
            if i == m or (i * 2) == m:
                return "YES"
            if check(i, m) == "NO":
                return check(i * 2, m)
            else:
                return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(check(n, m))
