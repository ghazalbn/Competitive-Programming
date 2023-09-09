#include <stdio.h>
#include <string.h>

int main() {
    int t;
    scanf("%d", &t);  // Read the number of test cases
    
    while (t--) {
        char s[300001];
        scanf("%s", s);  // Read the pattern string
        
        char result[300001];
        strcpy(result, s);
        char current = '0';
        
        for (int i = 0; i < strlen(s); i++) {
            if (s[i] == '?') {
                result[i] = current;
            } else {
                current = s[i];
            }
        }
        
        printf("%s\n", result);
    }
    
    return 0;
}
