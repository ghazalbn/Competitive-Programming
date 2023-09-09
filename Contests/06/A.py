t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    positive = 0

    for bi in b:
        if bi > 0:
            positive += 1
    negative = n - positive

    max_likes = list(range(1, positive + 1))
    i = positive - 1
    p = 0
    while p < negative: 
        max_likes.append(i)
        i -= 1
        p += 1
    min_likes = [1, 0] * negative + list(range(1, n -  (negative * 2) + 1))

    print(*max_likes)
    print(*min_likes)
