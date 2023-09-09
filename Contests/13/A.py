t = int(input())
for i in range(t):
    s = input()
    codeforces = "codeforces"
    count = 0
    for i in range(len(s)):
        if s[i] != codeforces[i]:
            count += 1
    print(count)
