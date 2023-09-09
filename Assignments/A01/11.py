t = int(input())

for _ in range(t):
    A, B, plus = 0, 0, 0
    mother, father, child = input().split()
    
    A = 1 if 'A' in mother or 'A' in father else 0
    B = 1 if 'B' in mother or 'B' in father else 0
    plus = 1 if '+' in mother or '+' in father else 0
    
    if '+' in child and not plus \
        or 'A' in child and not A \
        or 'B' in child and not B:
        print('invalid')
    else:
        print('valid')
