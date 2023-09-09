#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int k = 0; k < t; k++) {
        string s;
        cin >> s;
        int n = s.length();
        string sub = s.substr(0, n / 2);
        int count = 1;
        for (char i : sub) {
            if (i != sub[0]) {
                count = 2;
                break;
            }
        }

        if (count == 2) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
