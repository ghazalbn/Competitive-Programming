#include <iostream>
#include <vector>

using namespace std;

int longest_increasing_subsequence(vector<int>& a, int n) {
    vector<int> lis{a[0]};

    for (int i = 1; i < n; i++) {
        if (lis.back() >= a[i]) {
            int l = 0, r = lis.size()-1;
            while (l <= r) {
                int m = (l + r) / 2;
                if (lis[m] < a[i]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
            lis[l] = a[i];
        } else {
            lis.push_back(a[i]);
        }
    }

    return lis.size();
}

int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    cout << longest_increasing_subsequence(a, n) << endl;

    return 0;
}
