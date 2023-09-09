t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    if n % 2 == 1:
        print("-1")

    else:
        res = []
        l_count = 0
        cur = 1 if s[0] == '(' else 2

        for d in s:
            if d == '(':
                l_count += 1
                res.append(str(cur))
                cur = 1 if cur != 1 else 2
            else:
                res.append(str(cur))
                cur = 1 if cur != 2 else 2
        
        if l_count != n // 2:
            print(-1)
        else:
            print('2' if cur == 2 else '1')
            print(' '.join(res))
