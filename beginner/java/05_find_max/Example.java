/**
 * Challenge 05: Find Maximum
 * This file contains a working example solution.
 * Study it, then implement your own in Solution.java
 */
public class Example {
    
    /**
     * Find the maximum value in an array
     * 
     * Key concepts:
     * - Array traversal
     * - Comparison operators
     * - Tracking maximum value
     * - Conditional updates
     * 
     * Algorithm:
     * 1. Start with first element as max
     * 2. Compare each element with current max
     * 3. Update max if element is larger
     * 
     * @param arr The array of integers (at least one element)
     * @return The maximum value in the array
     */
    public static int findMax(int[] arr) {
        // Start with first element
        int max = arr[0];
        
        // Check remaining elements
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        
        return max;
    }
    
    public static void main(String[] args) {
        // Test cases
        System.out.println("findMax([3,7,2,9,1]) = " + 
            findMax(new int[]{3, 7, 2, 9, 1}));
        
        System.out.println("findMax([-5,-2,-10,-1]) = " + 
            findMax(new int[]{-5, -2, -10, -1}));
        
        System.out.println("findMax([42]) = " + 
            findMax(new int[]{42}));
        
        // Explanation
        System.out.println("\nStep-by-step with [3, 7, 2, 9, 1]:");
        System.out.println("1. max = 3 (first element)");
        System.out.println("2. 7 > 3, max = 7");
        System.out.println("3. 2 < 7, max stays 7");
        System.out.println("4. 9 > 7, max = 9");
        System.out.println("5. 1 < 9, max stays 9");
        System.out.println("Final: 9");
    }
}
