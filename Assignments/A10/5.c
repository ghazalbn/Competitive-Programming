#include <stdio.h>

int find_minimal_subsegment(int arr[], int l, int r) {
    int min_sum = 0;
    int curr_sum = 0;

    for (int i = l - 1; i < r; i++) {
        curr_sum += arr[i];
        min_sum = (min_sum > curr_sum) ? curr_sum : min_sum;
        curr_sum = (curr_sum < 0) ? curr_sum : 0;
    }

    return min_sum;
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    int array[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    for (int i = 0; i < q; i++) {
        int t, l, r;
        scanf("%d %d %d", &t, &l, &r);

        if (t == 1) {
            int min_sum = find_minimal_subsegment(array, l, r);
            printf("%d\n", min_sum);
        }
        else if (t == 2) {
            int idx = l;
            int x = r;
            array[idx - 1] = x;
        }
    }

    return 0;
}
