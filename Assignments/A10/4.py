def build_st(arr, tree, n):
    stack = [(0, 0, n-1)]

    while stack:
        node, start, end = stack.pop()

        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            stack.append((right_child, mid + 1, end))
            stack.append((left_child, start, mid))

            tree[node] = min(tree[left_child], tree[right_child])


def query_st(tree, node, start, end, left, right):
    if left > end or right < start:
        return float('inf')
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    left_min = query_st(tree, left_child, start, mid, left, right)
    right_min = query_st(tree, right_child, mid + 1, end, left, right)

    return min(left_min, right_min)


def update_st(tree, node, start, end, index, value):
    if start == end:
        tree[node] = value
        return

    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    if index <= mid:
        update_st(tree, left_child, start, mid, index, value)
    else:
        update_st(tree, right_child, mid + 1, end, index, value)

    tree[node] = min(tree[left_child], tree[right_child])


n, m = map(int, input().split())
a = list(map(int, input().split()))

segment_tree = [0] * (4 * n)

build_st(a, segment_tree, n)

for _ in range(m):
    q, xi, yi = map(int, input().split())

    if q == 1:
        result = query_st(segment_tree, 0, 0, n - 1, xi - 1, yi - 1)
        print(result)
    elif q == 2:
        a[xi - 1] = yi
        update_st(segment_tree, 0, 0, n - 1, xi - 1, yi)
