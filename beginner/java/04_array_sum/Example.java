/**
 * Challenge 04: Array Sum
 * This file contains a working example solution.
 * Study it, then implement your own in Solution.java
 */
public class Example {
    
    /**
     * Calculate the sum of all elements in an array
     * 
     * Key concepts:
     * - Array as parameter (int[])
     * - Array traversal with for loop
     * - Array length property
     * - Accumulator pattern
     * 
     * @param arr The array of integers
     * @return The sum of all elements
     */
    public static int arraySum(int[] arr) {
        int sum = 0;
        
        // Iterate through array
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        
        return sum;
        
        // Alternative: enhanced for loop
        // for (int num : arr) {
        //     sum += num;
        // }
    }
    
    public static void main(String[] args) {
        // Test cases
        System.out.println("arraySum([1,2,3,4,5]) = " + 
            arraySum(new int[]{1, 2, 3, 4, 5}));
        
        System.out.println("arraySum([-1,-2,-3]) = " + 
            arraySum(new int[]{-1, -2, -3}));
        
        System.out.println("arraySum([10]) = " + 
            arraySum(new int[]{10}));
        
        System.out.println("arraySum([]) = " + 
            arraySum(new int[]{}));
        
        // Explanation
        System.out.println("\nTwo ways to iterate:");
        System.out.println("1. Traditional: for (int i = 0; i < arr.length; i++)");
        System.out.println("2. Enhanced: for (int num : arr)");
    }
}
