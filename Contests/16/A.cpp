#include <iostream>

int main() {
    int t;
    std::cin >> t;  // number of testcases

    for (int i = 0; i < t; i++) {
        int x, k;
        std::cin >> x >> k;  // endpoint and jump constraint

        if (x % k != 0) {
            std::cout << 1 << std::endl;  // smallest number of moves
            std::cout << x << std::endl;  // jump distance
        } else {
            std::cout << 2 << std::endl;       // smallest number of moves
            std::cout << x - 1 << " " << 1 << std::endl;  // jump distances
        }
    }

    return 0;
}
