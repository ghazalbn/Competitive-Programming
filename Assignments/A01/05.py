y = int(input())

while True:
    y += 1
    s = set()
    if len(set(list(map(int, list(str(y)))))) == len(str(y)):
        print(y)
        break
