#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

long find_minimal_subsegment(const std::vector<long>& arr, int l, int r) {
    long min_sum = 0;
    long curr_sum = 0;

    for (int i = l - 1; i < r; i++) {
        curr_sum += arr[i];
        min_sum = std::min(min_sum, curr_sum);
        curr_sum = std::min(curr_sum, 0L);
    }

    return min_sum;
}

int main() {
    int n, q;
    std::cin >> n >> q;
    std::vector<long> array(n);

    for (int i = 0; i < n; i++) {
        std::cin >> array[i];
    }

    for (int i = 0; i < q; i++) {
        int t, l, r;
        std::cin >> t >> l >> r;

        if (t == 1) {
            long min_sum = find_minimal_subsegment(array, l, r);
            std::cout << min_sum << std::endl;
        }
        else if (t == 2) {
            int idx = l;
            long x = r;
            array[idx - 1] = x;
        }
    }

    return 0;
}
