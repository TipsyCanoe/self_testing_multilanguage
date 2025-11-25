#include <stdio.h>

/**
 * Challenge 07: String Length
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Calculate the length of a string (without using strlen)
 * 
 * @param str A null-terminated string
 * @return The number of characters in the string (not including '\0')
 * 
 * Key concepts:
 * - Strings in C (arrays of characters)
 * - Null terminator '\0'
 * - Pointer or array indexing
 * - Character counting
 * 
 * Important: Strings in C end with '\0' character
 */
int string_length(const char *str) {
    int length = 0;
    
    // Count characters until we hit null terminator
    while (str[length] != '\0') {
        length++;
    }
    
    return length;
}

int main() {
    // Test cases
    printf("string_length(\"hello\") = %d\n", string_length("hello"));
    printf("string_length(\"\") = %d\n", string_length(""));
    printf("string_length(\"C programming\") = %d\n", string_length("C programming"));
    printf("string_length(\"a\") = %d\n", string_length("a"));
    
    // Explanation
    printf("\nHow strings work in C:\n");
    printf("\"hello\" is stored as: h e l l o \\0\n");
    printf("                       0 1 2 3 4  5\n");
    printf("Length is 5 (we don't count \\0)\n");
    printf("\nAlgorithm:\n");
    printf("1. Start with length = 0\n");
    printf("2. While str[length] != '\\0':\n");
    printf("   - Increment length\n");
    printf("3. Return length\n");
    
    return 0;
}
