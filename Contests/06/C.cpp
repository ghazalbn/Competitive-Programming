#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<vector<int>> generate_blanket(int n, int m) {
    set<int> num_set;
    vector<vector<int>> B(n, vector<int>(m, 0));
    int num = 1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            B[i][j] = num;
            num_set.insert(num);
            num++;
        }
    }

    for (int i = 0; i < n - 3; i++) {
        for (int j = 0; j < m - 3; j++) {
            vector<vector<int>> A(4, vector<int>(4, 0));
            for (int x = 0; x < 4; x++) {
                for (int y = 0; y < 4; y++) {
                    A[x][y] = B[i + x][j + y];
                }
            }

            while (A[0][0] ^ A[0][1] ^ A[1][0] ^ A[1][1] != A[2][2] ^ A[2][3] ^ A[3][2] ^ A[3][3] || A[0][2] ^ A[0][3] ^ A[1][2] ^ A[1][3] != A[2][0] ^ A[2][1] ^ A[3][0] ^ A[3][1]) {
                swap(A[0][1], A[1][1]);
                swap(A[0][0], A[1][0]);
                swap(A[2][3], A[3][3]);
                swap(A[2][2], A[3][2]);
            }

            for (int x = 0; x < 4; x++) {
                for (int y = 0; y < 4; y++) {
                    B[i + x][j + y] = A[x][y];
                }
            }
        }
    }

    return { num_set.size(), B };
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, m;
        cin >> n >> m;

        auto blanket = generate_blanket(n, m);

        cout << blanket[0] << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cout << blanket[1][i][j] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}
