import math

def solve_test():
    n = int(input())
    v = int(math.sqrt(n))
    for k in range(2, v + 1):
        x = 1
        while math.pow(k, x - 1) <= n:
            x += 1
        for i in range(1, x + 1):
            m = (math.pow(k, i) - 1) // (k - 1)
            if m == n:
                print("YES")
                return
    print("NO")


t = int(input())
for _ in range(t):
    solve_test()