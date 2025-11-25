#include <stdio.h>
#include <limits.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

/**
 * Find the maximum value in an array
 * 
 * @param arr The array of integers
 * @param size The number of elements in the array (at least 1)
 * @return The maximum value in the array
 * 
 * TODO: Implement this function
 */
int find_max(int arr[], int size) {
    int result = INT_MIN; // Smallest possible int
    for (int i = 0; i < size; i++) {
        result = MAX(result, arr[i]);
    }
    return result;
}

int main() {
    // Test your function
    int arr1[] = {3, 7, 2, 9, 1};
    printf("find_max([3,7,2,9,1], 5) = %d\n", find_max(arr1, 5));
    
    int arr2[] = {-5, -2, -10, -1};
    printf("find_max([-5,-2,-10,-1], 4) = %d\n", find_max(arr2, 4));
    
    int arr3[] = {42};
    printf("find_max([42], 1) = %d\n", find_max(arr3, 1));
    
    return 0;
}
