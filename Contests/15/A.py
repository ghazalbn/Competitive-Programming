t = int(input())

for _ in range(t):
    n = int(input())
    flag = (n % 2 != 0)
    print(*[(i if flag else 2*i) for i in range(1, n + 1)])
    
