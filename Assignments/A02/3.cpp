#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> towers(n);
    vector<int> blocks;
    for (int i = 0; i < n; i++) {
        int m;
        cin >> m;
        towers[i].resize(m);
        for (int j = 0; j < m; j++) {
            cin >> towers[i][j];
            blocks.push_back(towers[i][j]);
        }
    }
    sort(blocks.begin(), blocks.end());
    map<int, int> b;
    for (int i = 0; i < blocks.size(); i++) {
        b[blocks[i]] = i;
    }

    int splits = 0;
    for (auto tower : towers) {
        for (int i = 0; i < tower.size() - 1; i++) {
            if (abs(b[tower[i + 1]] - b[tower[i]]) != 1) {
                splits++;
            }
        }
    }
    int merges = n + splits - 1;

    cout << splits << " " << merges << endl;
    return 0;
}
