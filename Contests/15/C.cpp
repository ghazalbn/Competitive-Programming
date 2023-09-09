#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MOD = 1000000007;

int main() {
    int t;
    cin >> t;

    for (int _ = 0; _ < t; ++_) {
        int n;
        cin >> n;

        vector<int> a(n), b(n);
        for (int i = 0; i < n; ++i)
            cin >> a[i];

        for (int i = 0; i < n; ++i)
            cin >> b[i];

        sort(a.rbegin(), a.rend());
        sort(b.rbegin(), b.rend());

        long long count = 1;
        int j = 0;
        for (int i = 0; i < n; ++i) {
            while (j < n && a[j] > b[i])
                ++j;
            count = (count * (j - i)) % MOD;
        }

        cout << count << endl;
    }

    return 0;
}
