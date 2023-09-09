def build_st(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        build_st(arr, tree, left_child, start, mid)
        build_st(arr, tree, right_child, mid + 1, end)

        tree[node] = tree[left_child] + tree[right_child]


def query_st(tree, node, start, end, left, right):
    if start > right or end < left:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_sum = query_st(tree, left_child, start, mid, left, right)
        right_sum = query_st(tree, right_child, mid + 1, end, left, right)

        return left_sum + right_sum


def update_st(tree, node, start, end, index, value):
    if start == end:
        tree[node] = value
    else:
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if index <= mid:
            update_st(tree, left_child, start, mid, index, value)
        else:
            update_st(tree, right_child, mid + 1, end, index, value)

        tree[node] = tree[left_child] + tree[right_child]


n, q = map(int, input().split())
array = list(map(int, input().split()))

tree = [0] * (4 * n)
build_st(array, tree, 0, 0, n - 1)

for _ in range(q):
    t, i, x = map(int, input().split())

    if t == 1:
        l, r = i, x
        interval_sum = query_st(tree, 0, 0, n - 1, l - 1, r - 1)
        print(interval_sum)
    elif t == 2:
        update_st(tree, 0, 0, n - 1, i - 1, x)
