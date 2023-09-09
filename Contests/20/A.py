t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    if x != 1:
        print("YES")
        print(n)
        print(" ".join(["1"] * n))
    elif n == 1 or k <= 1:
        print("NO")
    elif n % 2 == 0:
        print("YES")
        print(n // 2)
        print(" ".join(["2"] * (n // 2)))
    elif k > 2:
        print("YES")
        print((n - 3) // 2 + 1)
        print(" ".join(["2"] * ((n - 3) // 2)) + " 3")
    else:
        print("NO")
