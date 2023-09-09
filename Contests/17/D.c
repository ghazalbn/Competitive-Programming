#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        char s[100000];
        scanf("%s", s);

        if (n % 2 == 1) {
            printf("-1\n");
        } else {
            char res[100000];
            int left_cnt = 0;
            int current = (s[0] == '(') ? 1 : 2;
            int i = 0;

            for (i = 0; i < n; i++) {
                if (s[i] == '(') {
                    left_cnt++;
                    sprintf(&res[i], "%d", current);
                    current = (current != 1) ? 1 : 2;
                } else {
                    sprintf(&res[i], "%d", current);
                    current = (current != 2) ? 2 : 1;
                }
            }
            res[i] = '\0';

            if (left_cnt != n / 2) {
                printf("-1\n");
            } else {
                printf("%s\n", (current == 2) ? "2" : "1");
                printf("%s\n", res);
            }
        }
    }

    return 0;
}
