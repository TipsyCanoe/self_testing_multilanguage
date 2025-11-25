#include <stdio.h>

/**
 * Challenge 05: Array Sum
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Calculate the sum of all elements in an array
 * 
 * @param arr The array of integers
 * @param size The number of elements in the array
 * @return The sum of all elements
 * 
 * Key concepts:
 * - Array traversal
 * - Loop with array index
 * - Accumulator pattern
 * - Array size parameter
 */
int array_sum(int arr[], int size) {
    int sum = 0;
    
    // Iterate through each element
    for (int i = 0; i < size; i++) {
        sum += arr[i];  // Add current element to sum
    }
    
    return sum;
}

int main() {
    // Test case 1
    int arr1[] = {1, 2, 3, 4, 5};
    printf("array_sum([1,2,3,4,5], 5) = %d\n", array_sum(arr1, 5));
    
    // Test case 2: negative numbers
    int arr2[] = {-1, -2, -3};
    printf("array_sum([-1,-2,-3], 3) = %d\n", array_sum(arr2, 3));
    
    // Test case 3: single element
    int arr3[] = {10};
    printf("array_sum([10], 1) = %d\n", array_sum(arr3, 1));
    
    // Test case 4: empty array
    int arr4[] = {};
    printf("array_sum([], 0) = %d\n", array_sum(arr4, 0));
    
    // Explanation
    printf("\nHow it works:\n");
    printf("1. Initialize sum = 0\n");
    printf("2. Loop through array: i from 0 to size-1\n");
    printf("3. Add each arr[i] to sum\n");
    printf("4. Return final sum\n");
    
    return 0;
}
