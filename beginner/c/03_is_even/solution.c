#include <stdio.h>

/**
 * Determine if a number is even
 * 
 * @param n The number to check
 * @return 1 if n is even, 0 if n is odd
 * 
 * TODO: Implement this function
 */
int is_even(int n) {
    if (n % 2 ==0){
        return 1;
    } else {
        return 0;
    }
}

int main() {
    // Test your function
    printf("is_even(4) = %d\n", is_even(4));
    printf("is_even(7) = %d\n", is_even(7));
    printf("is_even(0) = %d\n", is_even(0));
    printf("is_even(-2) = %d\n", is_even(-2));
    return 0;
}
