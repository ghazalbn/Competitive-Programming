#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int dfs(vector<vector<int>>& dp, int n, int l) {
    if (dp[l][n] != 0) {
        return dp[l][n];
    }
    if (l == 1 || n == 1) {
        return n;
    }
    int ret = 0;
    for (int i = 1; i <= n; i++) {
        ret += dfs(dp, i, l - 1);
        ret %= MOD;
    }
    dp[l][n] = ret;
    return ret;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> dp(2 * m + 1, vector<int>(n + 1, 0));
    cout << dfs(dp, n, 2 * m) << endl;
    return 0;
}
