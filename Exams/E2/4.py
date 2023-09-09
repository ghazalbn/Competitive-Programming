n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(n - 2):
	for j in range(i+1, n - 1):
		for k in range(j+1, n):
			if a[j] > a[i] and a[j] > a[k]:
				count += 1

print(count)