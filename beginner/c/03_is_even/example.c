#include <stdio.h>

/**
 * Challenge 03: Is Even
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Determine if a number is even
 * 
 * @param n The number to check
 * @return 1 if n is even, 0 if n is odd
 * 
 * Key concepts:
 * - Modulo operator (%)
 * - Boolean values in C (1 = true, 0 = false)
 * - Comparison operators
 * 
 * A number is even if dividing by 2 leaves no remainder
 */
int is_even(int n) {
    return n % 2 == 0;
}

int main() {
    // Test cases
    int test_values[] = {4, 7, 0, -2, -3};
    int num_tests = 5;
    
    for (int i = 0; i < num_tests; i++) {
        int val = test_values[i];
        printf("is_even(%d) = %d\n", val, is_even(val));
    }
    
    // Explanation
    printf("\nHow it works:\n");
    printf("- n %% 2: remainder when dividing by 2\n");
    printf("- == 0: checks if remainder is 0\n");
    printf("- Result: 1 (true) or 0 (false)\n");
    printf("\nExamples:\n");
    printf("- 4 %% 2 = 0, so even (returns 1)\n");
    printf("- 7 %% 2 = 1, so odd (returns 0)\n");
    
    return 0;
}
