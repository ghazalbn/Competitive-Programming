t = int(input())
for _ in range(t):
    template = input()
    count = (9 if template[0] == '?' else 0 if template[0] == '0' else 1) * 10**template[1:].count('?')
    if count == 0:
        count += template[0] != '0'
    print(count)
