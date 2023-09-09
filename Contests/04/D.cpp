#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;
        vector<int> dist;
        for (int i = 0; i < n - 1; i++) {
            bool l = false;
            for (int j : dist) {
                if (s.substr(0, i) + s.substr(i + 2) == s.substr(0, j) + s.substr(j + 2)) {
                    l = true;
                    break;
                }
            }
            if (!l) {
                dist.push_back(i);
            }
        }
        cout << dist.size() << endl;
    }
    return 0;
}
