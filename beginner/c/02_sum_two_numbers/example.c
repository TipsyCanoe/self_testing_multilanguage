#include <stdio.h>

/**
 * Challenge 02: Sum Two Numbers
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Calculate the sum of two integers
 * 
 * @param a First integer
 * @param b Second integer
 * @return The sum of a and b
 * 
 * Key concepts:
 * - Function parameters
 * - Return values
 * - Integer arithmetic
 */
int sum(int a, int b) {
    return a + b;
}

int main() {
    // Test cases
    printf("sum(5, 3) = %d\n", sum(5, 3));
    printf("sum(-2, 7) = %d\n", sum(-2, 7));
    printf("sum(0, 0) = %d\n", sum(0, 0));
    printf("sum(-5, -3) = %d\n", sum(-5, -3));
    
    // Explanation
    printf("\nKey concepts:\n");
    printf("- int: integer type\n");
    printf("- Parameters: a and b\n");
    printf("- Return: a + b\n");
    printf("- %%d: format specifier for integers\n");
    
    return 0;
}
