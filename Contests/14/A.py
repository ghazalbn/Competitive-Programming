def get_remaining_members(n, k, stances):
    # count the number of opinions each member agrees with
    agree_counts = [0] * n
    for j in range(k):
        for i in range(n):
            if stances[i][j] == '+':
                agree_counts[i] += 1
    
    # sort the members in descending order based on their agreement count
    members = [(i, agree_counts[i]) for i in range(n)]
    members.sort(key=lambda x: x[1], reverse=True)
    
    # initialize a list of remaining members with all members
    remaining_members = set(range(n))
    
    # simulate the discussions and determine which members will stay or leave
    for j in range(k):
        num_agree = 0
        num_disagree = 0
        for i in remaining_members:
            if stances[i][j] == '+':
                num_agree += 1
            else:
                num_disagree += 1
        
        if num_agree > num_disagree:
            remaining_members = set([i for i in remaining_members if stances[i][j] == '+'])
        elif num_disagree > num_agree:
            remaining_members = set([i for i in remaining_members if stances[i][j] == '-'])
        else:
            remaining_members = set()
    
    # add ourselves to the remaining members set and return its size
    remaining_members.add(0)
    return len(remaining_members)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    stances = []
    for i in range(n):
        stances.append(input().strip())
    print(get_remaining_members(n, k, stances))
