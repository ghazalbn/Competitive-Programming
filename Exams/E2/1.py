n = int(input())
a = list(map(int, input().split()))
count = {}

for ai in a:
    count[ai] = count.get(ai, 0) + 1

sort_keys = list(count.keys())
sort_keys.sort(key=lambda x: count[x])

i = 0
l = []
flag = True
while len(a):
    if flag:
        if count[sort_keys[i]] > 0:
            a.remove(sort_keys[i])
            l.append(sort_keys[i])
            count[sort_keys[i]] -= 1
        else:
            i += 1
            continue
    if i < len(sort_keys) - 1 and count[sort_keys[i+1]] > 0:
        a.remove(sort_keys[i+1])
        count[sort_keys[i+1]] -= 1
        flag = True
    else:
        if count[sort_keys[i]] == 0:
            sort_keys.pop(i)
        i = -1
        flag = False
        continue
    if count[sort_keys[i]] == 0:
        sort_keys.pop(i)
    else:
        i += 1
    if i < len(sort_keys) - 1 and count[sort_keys[i+1]] == 0:
        sort_keys.pop(i+1)
    else:
        i += 1
    # i += 2
    if i == len(sort_keys):
        i = 0

print(len(set(l)))