#include <iostream>
#include <vector>
using namespace std;

int main() {
    long n, q;
    cin >> n;

    long* a = new long[n];
    for(long i = 0; i < n; i++) {
        cin >> a[i];
    }

    cin >> q;
    for(long i = 0; i < q; i++) {
        long s, k;
        cin >> s >> k;
        double result = 0;
        for(long j = s - 1; j < n; j += k) {
            result += a[j];
        }
        cout << result << endl;
    }

    delete[] a;
    return 0;
}
