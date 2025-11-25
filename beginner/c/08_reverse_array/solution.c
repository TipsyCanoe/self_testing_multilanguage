#include <stdio.h>

/**
 * Reverse an array in-place
 * 
 * @param arr The array of integers to reverse
 * @param size The number of elements in the array
 * 
 * TODO: Implement this function
 */
void reverse_array(int arr[], int size) {
    // Your code here
    for (int i = size - 1, j = 0; j < i; i--, j++) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
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
    // Test your function
    int arr1[] = {1, 2, 3, 4, 5};
    printf("Before: ");
    print_array(arr1, 5);
    reverse_array(arr1, 5);
    printf("After:  ");
    print_array(arr1, 5);
    
    return 0;
}
