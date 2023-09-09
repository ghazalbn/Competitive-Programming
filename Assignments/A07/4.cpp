#include <iostream>
#include <vector>
#include <queue>
using namespace std;

bool bfs(vector<vector<int>>& edges, int x, int n) {
    vector<bool> visited(n, false);
    queue<int> q;
    q.push(x);
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        if (!visited[node]) {
            visited[node] = true;
            for (int neighbor : edges[node]) {
                q.push(neighbor);
            }
        }
    }
    for (int v = 0; v < n; v++) {
        if (edges[v].size() > 0 && !visited[v]) {
            return false;
        }
    }
    return true;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> edges(n);
    vector<int> degree(n, 0);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges[u-1].push_back(v-1);
        edges[v-1].push_back(u-1);
        degree[u-1]++;
        degree[v-1]++;
    }

    bool hamband = true;
    for (int v = 0; v < n; v++) {
        if (edges[v].size() > 0 && !bfs(edges, v, n)) {
            hamband = false;
            break;
        }
    }

    int count = 0;
    for (int d : degree) {
        if (d % 2 == 1) {
            count++;
        }
    }
    if (count == 0 || count == 2) {
        if (hamband) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    } else {
        cout << "NO\n";
    }

    return 0;
}
