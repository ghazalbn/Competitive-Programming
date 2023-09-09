#include <iostream>

using namespace std;

const long long MOD = 7 + 1000000000;

long long power(long long base, long long exp) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % MOD;
        }
        base = (base * base) % MOD;
        exp /= 2;
    }
    return result;
}

long long inverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    int k, n;
    long long numerator = 1;
    long long denominator = 1;
    
    cin >> n >> k;
    for (int i = 1; i <= k; i++) {
        numerator = (numerator * (n - k + i)) % MOD;
        denominator = (denominator * i) % MOD;
    }
    long long result = (numerator * inverse(denominator)) % MOD;
    cout << result << endl;

    return 0;
}
