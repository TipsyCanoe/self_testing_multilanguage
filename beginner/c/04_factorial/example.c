#include <stdio.h>

/**
 * Challenge 04: Factorial
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Calculate the factorial of a non-negative integer
 * 
 * @param n A non-negative integer
 * @return n! (the factorial of n)
 * 
 * Key concepts:
 * - Loops (for loop)
 * - Accumulator pattern
 * - Edge case: 0! = 1
 * 
 * Factorial: n! = n × (n-1) × (n-2) × ... × 2 × 1
 * Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
 */
long factorial(int n) {
    // Base case: 0! = 1
    if (n == 0) {
        return 1;
    }
    
    // Calculate factorial using a loop
    long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    
    return result;
}

int main() {
    // Test cases
    int test_values[] = {0, 1, 5, 10};
    int num_tests = 4;
    
    for (int i = 0; i < num_tests; i++) {
        int n = test_values[i];
        printf("factorial(%d) = %ld\n", n, factorial(n));
    }
    
    // Explanation
    printf("\nHow it works:\n");
    printf("1. Start with result = 1\n");
    printf("2. Multiply by each number from 1 to n\n");
    printf("3. Special case: 0! = 1\n");
    printf("\nExample: 5!\n");
    printf("  1 × 1 = 1\n");
    printf("  1 × 2 = 2\n");
    printf("  2 × 3 = 6\n");
    printf("  6 × 4 = 24\n");
    printf("  24 × 5 = 120\n");
    
    return 0;
}
