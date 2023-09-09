import math

MOD = 998244353

n = int(input())
permutations = n
for i in range(1, n + 1):
    permutations = permutations * i % MOD

num = 1
permutations += 1
for i in range(n, 0, -1):
    permutations = (permutations - num) % MOD
    num = num * i % MOD
 
print(permutations % MOD)