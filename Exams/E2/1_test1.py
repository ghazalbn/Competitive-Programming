n = int(input())
a = list(map(int, input().split()))
count = {}

for ai in a:
    count[ai] = count.get(ai, 0) + 1

sort_keys = list(count.keys())
sort_keys.sort(key=lambda x: count[x])

i = 0
l = []
turn = 1
while len(a) > 0:
    if turn == 1 and count[sort_keys[i]] > 0:
        a.remove(sort_keys[i])
        count[sort_keys[i]] -= 1
        l.append(sort_keys[i])
        turn = 2
        # i = (i + 1) % len(sort_keys)
        continue
    if turn == 2 and count[sort_keys[i]] > 0:
        a.remove(sort_keys[i])
        count[sort_keys[i]] -= 1
        turn = 1
        continue
    
    i = (i + 1) % len(sort_keys)

print(len(set(l)))