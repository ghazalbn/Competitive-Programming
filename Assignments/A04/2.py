n = int(input())
a = list(map(int, input().split()))

count = [0] * n
count[0] = a[0]
count[1] = a[1]
# count[2] = min(a[1], a[n2])

for i in range(2, n):
    count[i] = min(count[i - 1], count[i - 2]) + a[i]

print(min(count[n - 1], count[n - 2]))
