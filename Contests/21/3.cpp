#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;

    // Process each scenario
    while (t--) {
        int R, U, L, D, k;
        cin >> R >> U >> L >> D >> k;

        int min_horizontal = min(R, L);
        int max_horizontal = max(R, L);
        int min_vertical = min(U, D);
        int max_vertical = max(U, D);

        if (min_horizontal <= min_vertical) {
            int com_k_horizontal = min(min_horizontal, k);
            min_horizontal -= com_k_horizontal;
            k -= com_k_horizontal;
            max_vertical += com_k_horizontal;

            if (k > 0) {
                int com_k_vertical = min(min_vertical, k);
                min_vertical -= com_k_vertical;
                k -= com_k_vertical;
                max_horizontal += com_k_vertical;
            }
        } else {
            int com_k_vertical = min(min_vertical, k);
            min_vertical -= com_k_vertical;
            k -= com_k_vertical;
            max_horizontal += com_k_vertical;

            if (k > 0) {
                int com_k_horizontal = min(min_horizontal, k);
                min_horizontal -= com_k_horizontal;
                k -= com_k_horizontal;
                max_vertical += com_k_horizontal;
            }
        }

        if (k > 0) {
            int min_common = min(max_vertical, max_horizontal);
            int max_common = max(max_vertical, max_horizontal);

            int com_k_common = min(min_common, k);
            max_common += com_k_common;
            max_vertical = max_common;
            min_common -= com_k_common;
            max_horizontal = min_common;
        }

        int distance_squared = ((max_horizontal - min_horizontal) * (max_horizontal - min_horizontal)) +
                               ((max_vertical - min_vertical) * (max_vertical - min_vertical));

        cout << distance_squared << endl;
    }

    return 0;
}
