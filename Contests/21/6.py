import itertools
from collections import Counter

hat = [0] * n
tshirt = [0] * n
pants = [0] * n

n = int(input())

for _ in range(n):
    ti, ci = map(int, input().split())
    
    if ti == 1:
        hat[ci] += 1
    elif ti == 2:
        tshirt[ci] += 1
    elif ti == 3:
        pants[ci] += 1

result = 0

for (ch, counth), (ct, countt), (cp, countp) in itertools.product(hat.items(), tshirt.items(), pants.items()):
    if ct != ch and cp != ct and cp != ch:
        result += counth * countp * countt

print(result)
