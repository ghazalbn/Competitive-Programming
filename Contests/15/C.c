#include <stdio.h>
#include <stdlib.h>

#define MOD (int)(1e9) + 7

int main() {
    int t;
    scanf("%d", &t);

    for (int x = 0; x < t; x++) {
        int n;
        scanf("%d", &n);

        int *a = (int *)malloc(n * sizeof(int));
        int *b = (int *)malloc(n * sizeof(int));

        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }

        for (int i = 0; i < n; i++) {
            scanf("%d", &b[i]);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (a[j] < a[j + 1]) {
                    int temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                }
                if (b[j] < b[j + 1]) {
                    int temp = b[j];
                    b[j] = b[j + 1];
                    b[j + 1] = temp;
                }
            }
        }

        long long count = 1;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j < n && a[j] > b[i]) {
                j++;
            }
            count = (count * (j - i)) % MOD;
        }

        printf("%lld\n", count);

        free(a);
        free(b);
    }

    return 0;
}
