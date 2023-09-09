import numpy as np

n = int(input())
p = np.array(list(map(int, input().split())))
p.sort()
mamur = max(0, sum(p) - (n - 1) * 100)
print(min(mamur, p[0]), max(p[0], mamur))
