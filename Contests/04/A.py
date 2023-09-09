t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    if s[0] != 'm' and s[0] != 'M':
        print("NO")
        continue

    i = 1
    while i < n and (s[i] == 'm' or s[i] == 'M'):
        i += 1

    j = i
    while j < n and (s[j] == 'e' or s[j] == 'E'):
        j += 1
    if j == 1 or j == n:
        print("NO")
        continue

    k = j
    while k < n and (s[k] == 'o' or s[k] == 'O'):
        k += 1
    if k == j or k == n:
        print("NO")
        continue

    l = k
    while l < n and (s[l] == 'w' or s[l] == 'W'):
        l += 1
    if l != n:
        print("NO")
        continue
    print("YES")
