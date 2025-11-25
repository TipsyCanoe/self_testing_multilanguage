#include <stdio.h>

/**
 * Challenge 06: Find Maximum
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Find the maximum value in an array
 * 
 * @param arr The array of integers (at least one element)
 * @param size The number of elements in the array
 * @return The maximum value in the array
 * 
 * Key concepts:
 * - Array traversal
 * - Comparison operators
 * - Tracking maximum value
 * - Updating variable conditionally
 */
int find_max(int arr[], int size) {
    // Start with first element as maximum
    int max = arr[0];
    
    // Check remaining elements
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    
    return max;
}

int main() {
    // Test case 1: mixed positive numbers
    int arr1[] = {3, 7, 2, 9, 1};
    printf("find_max([3,7,2,9,1], 5) = %d\n", find_max(arr1, 5));
    
    // Test case 2: all negative numbers
    int arr2[] = {-5, -2, -10, -1};
    printf("find_max([-5,-2,-10,-1], 4) = %d\n", find_max(arr2, 4));
    
    // Test case 3: single element
    int arr3[] = {42};
    printf("find_max([42], 1) = %d\n", find_max(arr3, 1));
    
    // Explanation
    printf("\nAlgorithm:\n");
    printf("1. Set max = arr[0] (first element)\n");
    printf("2. For each remaining element:\n");
    printf("   - If element > max, update max\n");
    printf("3. Return max\n");
    printf("\nExample with [3, 7, 2, 9, 1]:\n");
    printf("  max = 3 (start)\n");
    printf("  7 > 3, max = 7\n");
    printf("  2 < 7, max = 7\n");
    printf("  9 > 7, max = 9\n");
    printf("  1 < 9, max = 9 (final)\n");
    
    return 0;
}
