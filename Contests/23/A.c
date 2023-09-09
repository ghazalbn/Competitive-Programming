#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);  // Read the number of test cases
    
    while (t--) {
        int n;
        scanf("%d", &n);  // Read the number of nails
        
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            int height, length;
            scanf("%d %d", &height, &length);
            
            if (height > length) {
                count++;
            }
        }
        
        printf("%d\n", count);
    }
    
    return 0;
}
