#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, k, d, w;
        cin >> n >> k >> d >> w;

        vector<int> p(n);
        for (int j = 0; j < n; j++) {
            cin >> p[j];
        }

        int packs = 0, l = 0, r = 0;
        while (l < n) {
            r = l;
            while (r < n - 1 && r - l + 1 < k && p[r + 1] - p[l] - 1 < d + w) {
                    r++;
            }
            l = r + 1;
            packs++;
        }

        cout << packs << endl;
    }

    return 0;
}

