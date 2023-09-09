t = int(input())

for _ in range(t):
    a = input()
    b = input()
    m = len(a)
    n = len(b)
    if (a[0] == b[0]):
        print("YES")
        print(a[0] + '*')
    elif a[-1] == b[-1]:
        print("YES")
        print('*' + a[-1])
    else:
        longest = 0
        lcs = ''
        for i in range(1, m):
            for j in range(1, n):
                if a[i] == b[j] and a[i - 1] == b[j - 1]:
                    longest = 2
                    lcs = a[i - 1: i + 1]
                    break
                elif a[i] == b[j]:
                    longest = 1
                    lcs = a[i]
            if longest == 2:
                break


        if longest < 2:
            print("NO")
        else:
            print("YES")
            print('*' + lcs + '*')
