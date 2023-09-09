t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    t = input().strip()

    # check if s and t differ in the positions of some letters that are more than 3 positions apart
    for i in range(n):
        if abs(ord(s[i]) - ord(t[i])) > k:
            print("NO")
            break
    else:
        # check if s and t have a different number of occurrences of some letter
        for x in set(s + t):
            if s.count(x) != t.count(x):
                print("NO")
                break
        else:
            # check if s and t have the same number of occurrences of each letter,
            # and the positions of the letters that differ between s and t are all at a distance of 3 or 4
            for i in range(n):
                if s[i] != t[i]:
                    j = t.find(s[i])
                    if j == -1 or abs(i - j) not in (3, 4):
                        print("NO")
                        break
            else:
                print("YES")
