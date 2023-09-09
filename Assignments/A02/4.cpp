#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int f(int x) {
    // return to_string(x).length();
    return trunc(log10(x)) + 1;
}

int binary_search(vector<int>& arr, int l, int r, int x, int level) {
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if ((level == 1 && arr[mid] == x) || (level == 2 && f(arr[mid]) == x) || (level == 3 && f(f(arr[mid])) == x)) {
            return mid;
        } else if ((level == 1 && arr[mid] > x) || (level == 2 && f(arr[mid]) > x) || (level == 3 && f(f(arr[mid])) > x)) {
            return binary_search(arr, l, mid - 1, x, level);
        } else {
            return binary_search(arr, mid + 1, r, x, level);
        }
    } else {
        return -1;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n), b(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> b[i];
        }
        sort(b.begin(), b.end());

        int step = 0, i = 0;
        while (i != a.size()) {
            int mid = binary_search(b, 0, b.size() - 1, a[i], 1);
            if (mid != -1) {
                b.erase(b.begin() + mid);
                a.erase(a.begin() + i);
            } else {
                i++;
            }
        }

        i = 0;
        while (i != a.size()) {
            int mid = binary_search(b, 0, b.size() - 1, f(a[i]), 1);
            if (mid == -1) {
                mid = binary_search(b, 0, b.size() - 1, a[i], 2);
            }
            if (mid != -1) {
                b.erase(b.begin() + mid);
                a.erase(a.begin() + i);
                step++;
            } else {
                i++;
            }
        }

        i = 0;
        while (i != a.size()) {
            int mid = binary_search(b, 0, b.size() - 1, f(a[i]), 2);
            if (mid != -1) {
                b.erase(b.begin() + mid);
                a.erase(a.begin() + i);
                step += 2;
            } else {
                i++;
            }
        }

        i = 0;
        while (i != a.size()) {
            int mid = binary_search(b, 0, b.size() - 1, f(f(a[i])), 1);
            if (mid == -1) {
                mid = binary_search(b, 0, b.size() - 1, a[i], 3);
            }
            if (mid != -1) {
                b.erase(b.begin() + mid);
                a.erase(a.begin() + i);
                step += 2;
            } else {
                i++;
            }
        }

        i = 0;
        while (i != a.size()) {
            int mid = binary_search(b, 0, b.size() - 1, f(f(a[i])), 2);
            if (mid == -1) {
                mid = binary_search(b, 0, b.size() - 1, f(a[i]), 3);
            }
            if (mid != -1) {
                b.erase(b.begin() + mid);
                a.erase(a.begin() + i);
                step += 3;
            } else {
                i++;
            }
        }
    step += 4 * a.size();
    cout << step <<endl;
    }

    return 0;
}
