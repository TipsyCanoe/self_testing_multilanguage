#include <stdio.h>

/**
 * Calculate the factorial of a non-negative integer
 * 
 * @param n A non-negative integer
 * @return n! (the factorial of n)
 * 
 * TODO: Implement this function
 */
long factorial(int n) {
    if (n == 0) {
        return 1;
    }
    long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}


int main() {
    // Test your function
    printf("factorial(0) = %ld\n", factorial(0));
    printf("factorial(1) = %ld\n", factorial(1));
    printf("factorial(5) = %ld\n", factorial(5));
    printf("factorial(10) = %ld\n", factorial(10));
    return 0;
}
