#include <stdio.h>

/**
 * Challenge 09: Count Vowels
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Count the number of vowels in a string
 * 
 * @param str A null-terminated string
 * @return The number of vowels (a, e, i, o, u, A, E, I, O, U)
 * 
 * Key concepts:
 * - String traversal
 * - Character comparison
 * - Case-insensitive checking
 * - Multiple conditions (OR operator)
 */
int count_vowels(const char *str) {
    int count = 0;
    
    // Check each character
    for (int i = 0; str[i] != '\0'; i++) {
        char c = str[i];
        
        // Check if character is a vowel (upper or lowercase)
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            count++;
        }
    }
    
    return count;
}

int main() {
    // Test cases
    const char *tests[] = {"hello", "AEIOU", "xyz", "Programming"};
    int num_tests = 4;
    
    for (int i = 0; i < num_tests; i++) {
        printf("count_vowels(\"%s\") = %d\n", tests[i], count_vowels(tests[i]));
    }
    
    // Explanation
    printf("\nHow it works:\n");
    printf("1. Loop through each character\n");
    printf("2. Check if it's a vowel (a,e,i,o,u or A,E,I,O,U)\n");
    printf("3. If yes, increment count\n");
    printf("4. Return count\n");
    printf("\nExample: \"hello\"\n");
    printf("  h - not a vowel\n");
    printf("  e - vowel! count = 1\n");
    printf("  l - not a vowel\n");
    printf("  l - not a vowel\n");
    printf("  o - vowel! count = 2\n");
    
    return 0;
}
