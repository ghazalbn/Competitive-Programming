t = int(input())
for _ in range(t):
    n = int(input())
    if n == 4:
        print(26)
    else:
        l = 26

        increments = (2*i + 1 for i in range(5, n+1))
        l += (n-4)*(n+6)
        # l += sum(increments)
        print(l)
