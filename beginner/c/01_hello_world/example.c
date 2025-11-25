#include <stdio.h>

/**
 * Challenge 01: Hello World
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Print "Hello, World!" to the console
 * 
 * This is a simple function that demonstrates:
 * - Function definition in C
 * - Using printf for output
 * - Newline character \n
 */
void print_hello(void) {
    printf("Hello, World!\n");
}

int main() {
    // Call the function
    print_hello();
    
    // Additional examples
    printf("\nBreakdown:\n");
    printf("- void: function returns nothing\n");
    printf("- printf: outputs to console\n");
    printf("- \\n: newline character\n");
    
    return 0;
}
