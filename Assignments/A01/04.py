import numpy as np

n = int(input())
b = list(map(int, list(bin(n)[2:])))
b.reverse()
ones = np.where(b)[0]
x = len(ones)

print(x)
print(*ones)
