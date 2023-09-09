t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    current_space_length = 0
    longest_space_length = 0
    
    for i in range(n):
        if a[i] == 0:
            current_space_length += 1
        else:
            if current_space_length > longest_space_length:
                longest_space_length = current_space_length
            current_space_length = 0
    
    if current_space_length > longest_space_length:
        longest_space_length = current_space_length
        
    print(longest_space_length)
