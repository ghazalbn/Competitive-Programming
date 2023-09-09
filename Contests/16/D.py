t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    if n % 2 == 1:
        print("-1")

    else:
        res = []
        left_cnt = 0
        if s[0] == '(':
            current = 1 
        else:
            current = 2
        for c in s:
            if c == '(':
                left_cnt += 1
                res.append(str(current))
                current = 1 if current != 1 else 2
            else:
                res.append(str(current))
                current = 1 if current != 2 else 2
        
        if left_cnt != n // 2:
            print(-1)
        else:
            print('2' if current == 2 else '1')
            print(' '.join(res))
