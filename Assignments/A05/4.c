#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    long long a[n];
    for (int i = 0; i < n; i++) {
        scanf("%lld", &a[i]);
    }

    int q;
    scanf("%d", &q);

    for (int i = 0; i < q; i++) {
        int s, k;
        scanf("%d %d", &s, &k);
        long long result = 0;
        int end = (n - s) / k;
        for (register int j = 0; j <= end; j++) {
            result += a[j * k + s - 1];
        }
        printf("%lld\n", result);
    }

    return 0;
}
