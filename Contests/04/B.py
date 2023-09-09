# def count_burls(s, counts):
#     pairs = 0
#     for c in counts:
#         if c.islower():
#             pair_c = c.upper()
#             pairs += min(counts[c], counts[pair_c])
#     return pairs

# def maximize_burls(s, k):
#     counts = dict()
#     for c in s:
#         counts[c] = counts.get(c, 0) + 1
#         counts[op(c)] = counts.get(op(c), 0)

#     pairs = count_burls(s, counts)
#     if k == 0:
#         return pairs
#     for c in counts:
#         if c.islower():
#             pair_c = c.upper()
#             diff = int((counts[pair_c] - counts[c]) / 2)
#             if diff > 0 and k >= diff:
#                 k -= diff
#                 pairs += diff
#             elif diff < 0 and k >= -diff:
#                 k += diff
#                 pairs -= diff
#         elif c.isupper():
#             pair_c = c.lower()
#             diff = int((counts[pair_c] - counts[c]) / 2)
#             if diff > 0 and k >= diff:
#                 k -= diff
#                 pairs += diff
#             elif diff < 0 and k >= -diff:
#                 k += diff
#                 pairs -= diff
#         counts[c] = 0
#         counts[op(c)] = 0
#     return pairs

def op(c : chr):
    return c.upper() if c.islower() else c.lower()

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    # print(maximize_burls(s, k))
    counts = dict()
    for c in s:
        counts[c] = counts.get(c, 0) + 1
        counts[op(c)] = counts.get(op(c), 0)

    burl = 0
    for c, count in counts.items():
        a = min(count, counts[op(c)])
        burl += a
        if k:
            b = int((count + counts[op(c)]) / 2)
            burl += min(b - a, k)
            k -= b - a
        counts[c] = 0
        counts[op(c)] = 0

    print(burl)
