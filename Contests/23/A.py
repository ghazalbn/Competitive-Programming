t = int(input())

for _ in range(t):
    n = int(input())
    count = 0 
    for i in range(n):
        height, length = map(int, input().split())
        count += height > length
    print(count)
