#include <iostream>
#include <cstring>

using namespace std;

string check(int n, int m) {
    if (n == m) {
        return "YES";
    }
    for (int i = 1; i <= n / 2; i++) {
        if (n == i + (i * 2)) {
            if (i == m || (i * 2) == m) {
                return "YES";
            }
            if (check(i, m) == "NO") {
                return check(i * 2, m);
            } else {
                return "YES";
            }
        }
    }
    return "NO";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n, m;
        cin >> n >> m;
        cout << check(n, m) << endl;
    }
    return 0;
}
