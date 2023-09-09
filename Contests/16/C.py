t = int(input())

for _ in range(t):
    s = input()
    result = s
    current = '0'
    for i in range(len(s)):
        if s[i] == '?':
            result = result[:i] + current + result[i+1:]
        else:
            current = s[i]
    
    print(result)
