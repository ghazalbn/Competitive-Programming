def is_palindrome(arr):
    return arr == arr[::-1]

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [1, max(a)+1]
    for i in range(n//2):
        b.append(abs(a[i]-a[n-i-1]))
    b.sort(reverse=True)
    for x in b:
        f = [ai % x for ai in a]
        if is_palindrome(f):
            if x == max(a)+1:
                print(0)
                break
            else:
                print(x)
                break
    else:
        print(0)