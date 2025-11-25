#include <stdio.h>

/**
 * Count the number of vowels in a string
 * 
 * @param str A null-terminated string
 * @return The number of vowels (a, e, i, o, u, A, E, I, O, U)
 * 
 * TODO: Implement this function
 */
int count_vowels(const char *str) {
    int count = 0;
    while (*str != '\0') {
        char c = *str;
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            count++;
        }
        str++;
    }
    return count;
}

int main() {
    // Test your function
    printf("count_vowels(\"hello\") = %d\n", count_vowels("hello"));
    printf("count_vowels(\"AEIOU\") = %d\n", count_vowels("AEIOU"));
    printf("count_vowels(\"xyz\") = %d\n", count_vowels("xyz"));
    printf("count_vowels(\"Programming\") = %d\n", count_vowels("Programming"));
    return 0;
}
