#include <stdio.h>

/**
 * Calculate the length of a string (without using strlen)
 * 
 * @param str A null-terminated string
 * @return The number of characters in the string (not including '\0')
 * 
 * TODO: Implement this function without using strlen()
 */
int string_length(const char *str) {
    for (int length = 0; ; length++) {
        if (str[length] == '\0') {
            return length;
        }
    }
    return 0;
}

int main() {
    // Test your function
    printf("string_length(\"hello\") = %d\n", string_length("hello"));
    printf("string_length(\"\") = %d\n", string_length(""));
    printf("string_length(\"C programming\") = %d\n", string_length("C programming"));
    printf("string_length(\"a\") = %d\n", string_length("a"));
    return 0;
}
