a = input()
n = len(a)

count = [[0] * 2 for _ in range(n + 2)]
count[0][0] = 0

for i in range(1, n + 1):
    count[i][0] = count[i - 1][0] + int(a[i - 1].islower())
    count[n - i - 1][1] = count[n - i][1] + int(a[n - i].isupper())

r = min([count[i][0] + count[i][1] for i in range(0, n)])  
print(r)