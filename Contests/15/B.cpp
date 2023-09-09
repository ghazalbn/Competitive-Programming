#include <iostream>
#include <cmath>
using namespace std;

int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main() {
    int t;
    cin >> t;

    for (int _ = 0; _ < t; ++_) {
        int n;
        cin >> n;
        int p[n];
        for (int i = 0; i < n; ++i)
            cin >> p[i];

        int min_diff = abs(1 - p[0]);
        for (int i = 1; i < n; ++i) {
            int diff = abs(i + 1 - p[i]);
            if (diff != 0)
                min_diff = gcd(min_diff, diff);
        }

        cout << min_diff << endl;
    }

    return 0;
}
