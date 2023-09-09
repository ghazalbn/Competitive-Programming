def dfs(n, step):
    if n == 1:
        return True
    if step > 40:
        return False
    if n % 2 == 0:
        return False
    else:
        if dfs((n - 1) // 2, step + 1):
            path[step] = 2
            return True
        if dfs((n + 1) // 2, step + 1):
            path[step] = 1
            return True
    return False

t = int(input())

for i in range(t):
    n = int(input())
    path = [0] * 40
    s = 0
    if dfs(n, 0):
        for i in range(40):
            if path[i] == 0:
                s = i
                break
        print(s)
        print(*reversed(path[:s]))
    else:
        print("-1")