import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
print(len(np.where(a < 0)[0]) * (n - 1))
