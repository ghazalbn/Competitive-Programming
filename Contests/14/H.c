#include <stdio.h>

int count1(int num) {
    int count = 0;
    while (num > 0) {
        if (num & 1) {
            count++;
        }
        num >>= 1;
    }
    return count;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int b[n + 10];
    for (int i = 0; i < n + 10; i++) {
        b[i] = 0;
    }

    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        b[u] |= 1 << v;
        b[v] |= 1 << u;
    }

    int t = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (count1(b[i] & b[j]) > 2) {
                t = 1;
                break;
            }
        }
    }

    printf("%s\n", t ? "YES" : "NO");

    return 0;
}
