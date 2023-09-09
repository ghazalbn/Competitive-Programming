#include <stdio.h>
#include <stdbool.h>

#define MAX_TEST_CASES 1000
#define MAX_PARTICIPANTS 100
#define MAX_PROBLEMS 2000

struct pair {
    int first;
    int second;
};

long long binpow(long long a, long long b) {
    if (b == 0)
        return 1;

    long long res = binpow(a, b / 2);
    if (b % 2)
        return (res * res * a);
    else
        return res * res;
}

bool sortbyCond(const struct pair* a, const struct pair* b) {
    if (a->first != b->first)
        return (a->first < b->first);
    else
        return (a->second > b->second);
}

int main() {
    int test_cases;
    scanf("%d", &test_cases);
    while (test_cases--) {
        long long n, m, h;
        scanf("%lld %lld %lld", &n, &m, &h);

        struct pair vv[MAX_PARTICIPANTS]; // Assuming maximum size

        for (long long i = 0; i < n; i++) {
            int v[MAX_PROBLEMS]; // Assuming maximum size

            for (int j = 0; j < m; j++) {
                scanf("%lld", &v[j]);
            }

            // Sort the array
            for (int j = 0; j < m - 1; j++) {
                for (int k = 0; k < m - j - 1; k++) {
                    if (v[k] > v[k + 1]) {
                        int temp = v[k];
                        v[k] = v[k + 1];
                        v[k + 1] = temp;
                    }
                }
            }

            long long ans = 0;
            int s = 0;
            int j;
            for (j = 0; j < m; j++) {
                s += v[j];
                ans += s;
                if (s > h)
                    break;
            }
            if (j == m)
                j--;
            if (s > h) {
                j--;
                ans -= s;
            }

            vv[i].first = j;
            vv[i].second = ans;
        }

        // Sort the array of pairs
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (sortbyCond(&vv[j], &vv[j + 1])) {
                    struct pair temp = vv[j];
                    vv[j] = vv[j + 1];
                    vv[j + 1] = temp;
                }
            }
        }

        int final = 0;
        int pp = vv[0].first;
        int ppx = vv[0].second;

        for (int i = 0; i < n; i++) {
            final++;
            if (vv[i].first == pp && vv[i].second == ppx) {
                break;
            }
        }

        printf("%d\n", final);
    }

    return 0;
}
