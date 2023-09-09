#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<int> b(3000, 0);
    
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        b[u] |= 1 << v;
        b[v] |= 1 << u;
    }
    
    bool t = false;
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (bitset<32>(b[i] & b[j]).count() > 2) {
                t = true;
                break;
            }
        }
        if (t) {
            break;
        }
    }
    
    cout << (t ? "YES" : "NO") << endl;
    
    return 0;
}
