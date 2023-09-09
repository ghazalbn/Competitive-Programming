#include <iostream>
#include <vector>
#include <deque>
using namespace std;

void find_parent(vector<vector<int>>& adj, vector<int>& visited, vector<int>& parent, int node) {
    visited[node] = 1;
    deque<int> stack;
    stack.push_back(node);

    while (!stack.empty()) {
        int curr = stack.back();
        stack.pop_back();
        for (int neighbor : adj[curr]) {
            if (visited[neighbor] == 0) {
                visited[neighbor] = 1;
                parent[neighbor] = curr;
                stack.push_back(neighbor);
            }
        }
    }
}

void dfs(vector<vector<int>>& adj, int s, vector<int>& dp, vector<int>& loc, vector<int>& visited) {
    visited[s] = 1;
    deque<pair<int, int>> stack;
    stack.push_back({s, dp[s]});

    while (!stack.empty()) {
        int curr = stack.back().first;
        int dist = stack.back().second;
        stack.pop_back();
        for (int neighbor : adj[curr]) {
            if (visited[neighbor] == 0) {
                visited[neighbor] = 1;
                dp[neighbor] = (loc[curr] > loc[neighbor]) ? dist + 1 : dist;
                stack.push_back({neighbor, dp[neighbor]});
            }
        }
    }
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> adj(n);
        vector<int> loc(n, 0);
        vector<pair<int, int>> edges;
        vector<int> parent(n, -1);

        for (int i = 0; i < n - 1; i++) {
            int u, v;
            cin >> u >> v;
            u--, v--;
            adj[u].push_back(v);
            adj[v].push_back(u);
            edges.push_back({u, v});
        }

        vector<int> visited(n, 0);
        find_parent(adj, visited, parent, 0);

        for (int i = 0; i < edges.size(); i++) {
            int u = edges[i].first, v = edges[i].second;
            if (u == parent[v]) {
                loc[v] = i;
            }
            else {
                loc[u] = i;
            }
        }

        vector<int> dp(n, 0);
        visited.assign(n, 0);
        dfs(adj, 0, dp, loc, visited);

        int max_length = *max_element(dp.begin(), dp.end()) + 1;
        cout << max_length << endl;
    }

    return 0;
}
