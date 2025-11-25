#include <stdio.h>

/**
 * Challenge 08: Reverse Array
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Reverse an array in-place
 * 
 * @param arr The array of integers to reverse
 * @param size The number of elements in the array
 * 
 * Key concepts:
 * - In-place modification (no new array)
 * - Two-pointer technique
 * - Swapping elements
 * - Array indexing from both ends
 * 
 * Algorithm: Swap elements from both ends moving towards center
 */
void reverse_array(int arr[], int size) {
    int left = 0;
    int right = size - 1;
    
    // Swap elements from both ends
    while (left < right) {
        // Swap arr[left] and arr[right]
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        
        // Move pointers
        left++;
        right--;
    }
}

// Helper function to print array
void print_array(int arr[], int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]\n");
}

int main() {
    // Test case 1
    int arr1[] = {1, 2, 3, 4, 5};
    printf("Before: ");
    print_array(arr1, 5);
    reverse_array(arr1, 5);
    printf("After:  ");
    print_array(arr1, 5);
    
    // Explanation
    printf("\nAlgorithm (two-pointer):\n");
    printf("Start: [1, 2, 3, 4, 5]\n");
    printf("       left=0  right=4\n");
    printf("Swap 1↔5: [5, 2, 3, 4, 1]\n");
    printf("       left=1  right=3\n");
    printf("Swap 2↔4: [5, 4, 3, 2, 1]\n");
    printf("       left=2  right=2\n");
    printf("Stop (left >= right)\n");
    
    return 0;
}
