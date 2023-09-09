#include <iostream>
#include <vector>
using namespace std;

int find(vector<int>& parent, int i) {
    if (parent[i] != i) {
        parent[i] = find(parent, parent[i]);
    }
    return parent[i];
}

void unionSet(vector<int>& parent, vector<int>& rank, int i, int j) {
    int i_root = find(parent, i);
    int j_root = find(parent, j);
    if (i_root == j_root) {
        return;
    }
    if (rank[i_root] < rank[j_root]) {
        parent[i_root] = j_root;
    } else if (rank[i_root] > rank[j_root]) {
        parent[j_root] = i_root;
    } else {
        parent[j_root] = i_root;
        rank[i_root] += 1;
    }
}

int main() {
    int n, q;
    cin >> n >> q;
    vector<int> parent(n + 1);
    vector<int> rank(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < q; i++) {
        int op_type, x, y;
        cin >> op_type >> x >> y;
        if (op_type == 1) {
            unionSet(parent, rank, x, y);
        } else if (op_type == 2) {
            for (int j = x; j < y; j++) {
                unionSet(parent, rank, j, j + 1);
            }
        } else if (op_type == 3) {
            if (find(parent, x) == find(parent, y)) {
                cout << "YES\n";
            } else {
                cout << "NO\n";
            }
        }
    }

    return 0;
}
