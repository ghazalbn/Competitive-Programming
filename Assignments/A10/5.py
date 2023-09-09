class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.min_sum = float('inf')
        self.sum = 0
        self.left = None
        self.right = None

def build_segment_tree(arr, start, end):
    if start == end:
        node = SegmentTreeNode(start, end)
        node.min_sum = arr[start]
        node.sum = arr[start]
        return node

    mid = (start + end) // 2
    left_child = build_segment_tree(arr, start, mid)
    right_child = build_segment_tree(arr, mid + 1, end)

    node = SegmentTreeNode(start, end)
    node.left = left_child
    node.right = right_child
    node.min_sum = min(left_child.min_sum, right_child.min_sum)
    node.sum = left_child.sum + right_child.sum

    return node

def propagate(node):
    if node.start != node.end:
        if node.left is None:
            mid = (node.start + node.end) // 2
            node.left = SegmentTreeNode(node.start, mid)
            node.right = SegmentTreeNode(mid + 1, node.end)

        node.left.min_sum = min(node.left.min_sum, node.min_sum)
        node.right.min_sum = min(node.right.min_sum, node.min_sum)

def range_query(node, start, end, l, r):
    if start > r or end < l:
        return float('inf')

    if l <= start and end <= r:
        return node.min_sum

    mid = (start + end) // 2
    left_min = range_query(node.left, start, mid, l, r)
    right_min = range_query(node.right, mid + 1, end, l, r)

    return min(left_min, right_min)

def update(node, index, value):
    if node.start == node.end:
        node.min_sum = value
        node.sum = value
        return

    mid = (node.start + node.end) // 2

    if index <= mid:
        update(node.left, index, value)
    else:
        update(node.right, index, value)

    node.min_sum = min(node.left.min_sum, node.right.min_sum)
    node.sum = node.left.sum + node.right.sum

n, q = map(int, input().split())
array = list(map(int, input().split()))
tree = build_segment_tree(array, 0, n - 1)

for _ in range(q):
    t, l, r = map(int, input().split())

    if t == 1:
        min_sum = range_query(tree, 0, n - 1, l - 1, r - 1)
        print(min(min_sum, 0))
    elif t == 2:
        i, x = l, r
        update(tree, i - 1, x)
        propagate(tree)
