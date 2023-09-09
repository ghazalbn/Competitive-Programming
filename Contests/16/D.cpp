#include <iostream>
#include <string>
#include <vector>

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        int n;
        std::cin >> n;
        
        std::string s;
        std::cin >> s;

        if (n % 2 == 1) {
            std::cout << "-1" << std::endl;
        } else {
            std::vector<std::string> res;
            int left_cnt = 0;
            int current = (s[0] == '(') ? 1 : 2;

            for (char c : s) {
                if (c == '(') {
                    left_cnt++;
                    res.push_back(std::to_string(current));
                    current = (current != 1) ? 1 : 2;
                } else {
                    res.push_back(std::to_string(current));
                    current = (current != 2) ? 2 : 1;
                }
            }

            if (left_cnt != n / 2) {
                std::cout << "-1" << std::endl;
            } else {
                std::cout << ((current == 2) ? "2" : "1") << std::endl;
                for (const std::string& num : res) {
                    std::cout << num << " ";
                }
                std::cout << std::endl;
            }
        }
    }

    return 0;
}
