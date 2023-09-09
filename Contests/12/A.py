# t = int(input())

# for _ in range(t):
#     n = int(input())
#     statements = list(map(int, input().split()))
#     statements.sort()

#     inconsistent = True
#     for i in range(n):
#         s = statements[i]
#         # liars = n - statements[i:].count(s)
#         liars = s 
#         while liars > 0 and statements[:liars][-1] != statements[liars:][0]:
#             liars -= 1
#         if statements[liars + 1] != s:
#         # if s <= liars :
#             inconsistent = False
#             print(n - liars -1)
#             break
#     if inconsistent:
#         print(-1)

t = int(input())
 
for _ in range(t):
    n = int(input())
    statements = list(map(int, input().split()))
    statements.sort()
 
    inconsistent = True
    for i in range(n):
        s = statements[i]
        liars = len(statements[i:]) - statements[i:].count(s)
        if s <= liars :
            inconsistent = False
            print(liars)
            break
    if inconsistent:
        print(-1)