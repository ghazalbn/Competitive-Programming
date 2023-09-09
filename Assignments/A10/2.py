import math

n, q = map(int, input().split())
array = list(map(int, input().split()))

block_size = int(math.sqrt(n))
num_blocks = math.ceil(n / block_size)
blocks = [0] * num_blocks

for i in range(n):
    block_index = i // block_size
    blocks[block_index] += array[i]


for _ in range(q):
    t, i, x = map(int, input().split())

    if t == 1:
        l, r = i, x
        l_block = (l - 1) // block_size
        r_block = (r - 1) // block_size
        interval_sum = 0

        if l_block == r_block:
            for j in range(l - 1, r):
                interval_sum += array[j]
        else:
            for j in range(l - 1, (l_block + 1) * block_size):
                interval_sum += array[j]
            for block in range(l_block + 1, r_block):
                interval_sum += blocks[block]
            for j in range(r_block * block_size, r):
                interval_sum += array[j]
        
        print(interval_sum)
    elif t == 2:
        block_index = (i - 1) // block_size
        blocks[block_index] += x - array[i - 1]
        array[i - 1] = x
