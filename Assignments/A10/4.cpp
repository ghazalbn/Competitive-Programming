#include <iostream>
#include <vector>
#include <limits>
using namespace std;

void build_st(const vector<int>& arr, vector<int>& tree, int node, int start, int end) {
    if (start == end) {
        tree[node] = arr[start];
        return;
    }

    int mid = (start + end) / 2;
    int left_child = 2 * node;
    int right_child = 2 * node + 1;

    build_st(arr, tree, left_child, start, mid);
    build_st(arr, tree, right_child, mid + 1, end);

    tree[node] = min(tree[left_child], tree[right_child]);
}

int query_st(const vector<int>& tree, int node, int start, int end, int left, int right) {
    if (left > end || right < start)
        return numeric_limits<int>::max();
    if (left <= start && right >= end)
        return tree[node];

    int mid = (start + end) / 2;
    int left_child = 2 * node;
    int right_child = 2 * node + 1;

    int left_min = query_st(tree, left_child, start, mid, left, right);
    int right_min = query_st(tree, right_child, mid + 1, end, left, right);

    return min(left_min, right_min);
}

void update_st(vector<int>& tree, int node, int start, int end, int index, int value) {
    if (start == end) {
        tree[node] = value;
        return;
    }

    int mid = (start + end) / 2;
    int left_child = 2 * node;
    int right_child = 2 * node + 1;

    if (index <= mid)
        update_st(tree, left_child, start, mid, index, value);
    else
        update_st(tree, right_child, mid + 1, end, index, value);

    tree[node] = min(tree[left_child], tree[right_child]);
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];

    vector<int> segment_tree(4 * n, 0);
    build_st(a, segment_tree, 1, 0, n - 1);

    for (int i = 0; i < m; i++) {
        int q, xi, yi;
        cin >> q >> xi >> yi;

        if (q == 1) {
            int result = query_st(segment_tree, 1, 0, n - 1, xi - 1, yi - 1);
            cout << result << endl;
        } else if (q == 2) {
            a[xi - 1] = yi;
            update_st(segment_tree, 1, 0, n - 1, xi - 1, yi);
        }
    }

    return 0;
}
