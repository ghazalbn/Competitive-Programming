#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int u;
    int v;
} Edge;

typedef struct {
    int node;
    int dist;
} StackItem;

typedef struct {
    int *arr;
    int front;
    int rear;
} Deque;

void initDeque(Deque *deque, int size) {
    deque->arr = (int *)malloc(sizeof(int) * size);
    deque->front = -1;
    deque->rear = -1;
}

int isEmpty(Deque *deque) {
    return (deque->front == -1 && deque->rear == -1);
}

void pushBack(Deque *deque, int item) {
    if (isEmpty(deque)) {
        deque->front = 0;
        deque->rear = 0;
    } else {
        deque->rear = (deque->rear + 1) % size;
    }
    deque->arr[deque->rear] = item;
}

int popBack(Deque *deque) {
    int item = deque->arr[deque->rear];
    if (deque->front == deque->rear) {
        deque->front = -1;
        deque->rear = -1;
    } else {
        deque->rear = (deque->rear - 1 + size) % size;
    }
    return item;
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        int **adj = (int **)malloc(sizeof(int *) * n);
        for (int i = 0; i < n; i++) {
            adj[i] = (int *)malloc(sizeof(int) * n);
            for (int j = 0; j < n; j++) {
                adj[i][j] = 0;
            }
        }

        int *loc = (int *)malloc(sizeof(int) * n);
        for (int i = 0; i < n; i++) {
            loc[i] = 0;
        }

        Edge *edges = (Edge *)malloc(sizeof(Edge) * (n - 1));

        int *parent = (int *)malloc(sizeof(int) * n);
        for (int i = 0; i < n; i++) {
            parent[i] = -1;
        }

        for (int i = 0; i < n - 1; i++) {
            int u, v;
            scanf("%d %d", &u, &v);
            u--, v--;
            adj[u][v] = 1;
            adj[v][u] = 1;
            edges[i].u = u;
            edges[i].v = v;
        }

        int *visited = (int *)malloc(sizeof(int) * n);
        for (int i = 0; i < n; i++) {
            visited[i] = 0;
        }

        Deque stack;
        initDeque(&stack, n);
        pushBack(&stack, 0);

        while (!isEmpty(&stack)) {
            int curr = popBack(&stack);
            visited[curr] = 1;

            for (int neighbor = 0; neighbor < n; neighbor++) {
                if (adj[curr][neighbor] && !visited[neighbor]) {
                    pushBack(&stack, neighbor);
                    parent[neighbor] = curr;
                }
            }
        }

        for (int i = 0; i < n - 1; i++) {
            int u = edges[i].u, v = edges[i].v;
            if (u == parent[v]) {
                loc[v] = i;
            } else {
                loc[u] = i;
            }
        }

        int *dp = (int *)malloc(sizeof(int) * n);
        for (int i = 0; i < n; i++) {
            dp[i] = 0;
        }

        for (int i = 0; i < n; i++) {
            visited[i] = 0;
        }

        initDeque(&stack, n);
        pushBack(&stack, 0);
        dp[0] = 0;

        while (!isEmpty(&stack)) {
            int curr = popBack(&stack).node;
            int dist = popBack(&stack).dist;
            visited[curr] = 1;

            for (int neighbor = 0; neighbor < n; neighbor++) {
                if (adj[curr][neighbor] && !visited[neighbor]) {
                    dp[neighbor] = (loc[curr] > loc[neighbor]) ? dist + 1 : dist;
                    pushBack(&stack, neighbor);
                    pushBack(&stack, dp[neighbor]);
                }
            }
        }

        int max_length = dp[0];
        for (int i = 1; i < n; i++) {
            if (dp[i] > max_length) {
                max_length = dp[i];
            }
        }
        printf("%d\n", max_length + 1);

        free(visited);
        free(dp);
        for (int i = 0; i < n; i++) {
            free(adj[i]);
        }
        free(adj);
        free(loc);
        free(edges);
        free(parent);
    }

    return 0;
}
