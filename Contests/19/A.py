t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x, y = n, 0
    result = "NO"
    while x >= 0:
        if x * (x - 1) // 2 + y * (y - 1) // 2 == k:
            result = "YES"
            break
        x -= 1
        y += 1
    print(result)
    if result == "YES":
        for i in range(x):
            print("1", end="")
            if i != x - 1:
                print(" ", end="")
        if x and y:
            print(" ", end="")
        for j in range(y):
            print("-1", end=" ")
            if j != y - 1:
                print(" ", end="")
        print()
