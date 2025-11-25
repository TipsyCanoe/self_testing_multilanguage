#include <stdio.h>

/**
 * Calculate the sum of two integers
 * 
 * @param a First integer
 * @param b Second integer
 * @return The sum of a and b
 * 
 * TODO: Implement this function
 */
int sum(int a, int b) {
    return a + b;
}

int main() {
    // Test your function
    printf("sum(5, 3) = %d\n", sum(5, 3));
    printf("sum(-2, 7) = %d\n", sum(-2, 7));
    printf("sum(0, 0) = %d\n", sum(0, 0));
    return 0;
}
