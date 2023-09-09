#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    map<int, int> hat;
    map<int, int> tshirt;
    map<int, int> pants;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int ti, ci;
        cin >> ti >> ci;

        if (ti == 1) {
            hat[ci]++;
        } else if (ti == 2) {
            tshirt[ci]++;
        } else if (ti == 3) {
            pants[ci]++;
        }
    }

    int result = 0;

    for (auto& h : hat) {
        for (auto& t : tshirt) {
            for (auto& p : pants) {
                if (t.first != h.first && p.first != t.first && p.first != h.first) {
                    result += h.second * t.second * p.second;
                }
            }
        }
    }

    cout << result << endl;

    return 0;
}
