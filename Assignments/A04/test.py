from heapq import heappush, heappop

def find_shortest_sorting_time(n, k, lengths):
    min_heap = []
    for length in lengths:
        heappush(min_heap, length)

    total_time = 0
    while len(min_heap) > 1:
        part1 = heappop(min_heap)
        part2 = heappop(min_heap)
        total_time += part1 + part2
        heappush(min_heap, part1 + part2)

    return total_time

n, k = map(int, input().split())
lengths = list(map(int, input().split()))
result = find_shortest_sorting_time(n, k, lengths)
print(result)