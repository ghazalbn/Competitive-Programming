t = int(input())
for i in range(t):
    n = int(input())
    prefixes_suffixes = input().split()

    prefixes_suffixes.sort(key=len, reverse=True)
    prefix = prefixes_suffixes[0]
    suffix = prefixes_suffixes[1]
    
    if prefix[1:] == suffix[:-1]:
        s = prefix + suffix[-1]
    else:
        s = suffix + prefix[-1]
    
    if s != s[::-1]:
        print("NO")
    else:
        print("YES")
