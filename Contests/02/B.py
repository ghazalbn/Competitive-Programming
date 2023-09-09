import math

t = int(input())

for _ in range(t):
    tuples = []
    n = int(input())
    a = list(map(int, input().split()))
    b = [(a[i], i) for i in range(len(a))]
    b.sort()
    if (a.count(1) == n):
        print(0)
    elif(0 < a.count(1)):
        print(-1)
    else:
        while b[0][0] != b[-1][0]:
            b[-1] = (math.ceil(b[-1][0] / b[0][0]), b[-1][1])
            tuples.append((b[-1][1] + 1, b[0][1] + 1))
            b.sort()

        print(len(tuples))
        for i in range(len(tuples)): 
            print(*tuples[i], sep=' ')
