#include <stdio.h>

/**
 * Calculate the sum of all elements in an array
 * 
 * @param arr The array of integers
 * @param size The number of elements in the array
 * @return The sum of all elements
 * 
 * TODO: Implement this function
 */
int array_sum(int arr[], int size) {
    int sum = 0;
    if (size <= 0) {
        return 0;
    } else if (size == 1) {
        return arr[0];
    }
    for (int i =0; i < size; i++) {

        sum += arr[i];
    }
    return sum;
}

int main() {
    // Test your function
    int arr1[] = {1, 2, 3, 4, 5};
    printf("array_sum([1,2,3,4,5], 5) = %d\n", array_sum(arr1, 5));
    
    int arr2[] = {-1, -2, -3};
    printf("array_sum([-1,-2,-3], 3) = %d\n", array_sum(arr2, 3));
    
    int arr3[] = {10};
    printf("array_sum([10], 1) = %d\n", array_sum(arr3, 1));
    
    return 0;
}
