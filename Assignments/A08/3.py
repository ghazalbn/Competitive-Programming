from collections import defaultdict, deque

T = int(input())
for _ in range(T):
    n, m, s, t = map(int, input().split())
    adj_list = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)

    visited = set()
    queue = deque([(t, 0)])

    # BFS
    while queue:
        friend, day = queue.popleft()
        if friend == s and day != 0:
            print(day)
            break

        visited.add(friend)
        for adj_friend in adj_list[friend]:
            if adj_friend not in visited:
                queue.append((adj_friend, day + 1))
    else:
        print(-1)
