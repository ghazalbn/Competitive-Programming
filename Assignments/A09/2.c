#include <stdio.h>
#include <stdlib.h>

int find(int parent[], int i) {
    if (parent[i] != i) {
        parent[i] = find(parent, parent[i]);
    }
    return parent[i];
}

void unionSet(int parent[], int rank[], int i, int j) {
    int iRoot = find(parent, i);
    int jRoot = find(parent, j);
    if (iRoot == jRoot) {
        return;
    }
    if (rank[iRoot] < rank[jRoot]) {
        parent[iRoot] = jRoot;
    } else if (rank[iRoot] > rank[jRoot]) {
        parent[jRoot] = iRoot;
    } else {
        parent[jRoot] = iRoot;
        rank[iRoot]++;
    }
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);

    int *parent = malloc((n+1) * sizeof(int));
    int *rank = calloc(n+1, sizeof(int));

    for (int i = 0; i <= n; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < q; i++) {
        int op_type, x, y;
        scanf("%d %d %d", &op_type, &x, &y);

        if (op_type == 1) {
            unionSet(parent, rank, x, y);
        } else if (op_type == 2) {
            int root_x = find(parent, x);
            for (int j = x + 1; j <= y; j++) {
                unionSet(parent, rank, root_x, j);
            }
        } else if (op_type == 3) {
            if (find(parent, x) == find(parent, y)) {
                printf("YES\n");
            } else {
                printf("NO\n");
            }
        }
    }

    free(parent);
    free(rank);

    return 0;
}
