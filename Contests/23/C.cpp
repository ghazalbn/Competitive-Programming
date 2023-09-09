#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cansort(const pair<int, int>& a, const pair<int, int>& b) {
    if (a.first != b.first)
        return (a.first < b.first);
    else
        return (a.second > b.second);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n, m, h;
        cin >> n >> m >> h;

        vector<pair<int, int>> vv;

        int pp = 0, ppx = 0; // Declare and initialize pp and ppx

        for (int i = 0; i < n; i++) {
            vector<int> v;
            for (int j = 0; j < m; j++) {
                int x;
                cin >> x;
                v.push_back(x);
            }
            sort(v.begin(), v.end());

            int ans = 0, s = 0, j = 0;
            for (j = 0; j < m; j++) {
                s += v[j];
                ans += s;
                if (s > h)
                    break;
            }
            if (j == m) j--;
            if (s > h) {
                j--;
                ans -= s;
            }

            vv.push_back({ j, ans });

            if (i == 0) {
                pp = j;
                ppx = ans;
            }
        }

        sort(vv.rbegin(), vv.rend(), cansort);

        int final = 0;
        for (auto it : vv) {
            final++;
            if (it.first == pp && it.second == ppx) {
                break;
            }
        }

        cout << final << "\n";
    }

    return 0;
}
