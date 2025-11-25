/**
 * Challenge 04: Array Sum
 * TODO: Implement the arraySum method
 */
public class Solution {
    
    /**
     * Calculate the sum of all elements in an array
     * 
     * @param arr The array of integers
     * @return The sum of all elements
     */
    public static int arraySum(int[] arr) {
        int result = 0;
        for (int i = 0; i < arr.length; i++) {
            result += arr[i];
        }
        return result;
    }
    
    public static void main(String[] args) {
        // Test your method
        System.out.println("arraySum([1,2,3,4,5]) = " + arraySum(new int[]{1, 2, 3, 4, 5}));
        System.out.println("arraySum([-1,-2,-3]) = " + arraySum(new int[]{-1, -2, -3}));
        System.out.println("arraySum([10]) = " + arraySum(new int[]{10}));
        System.out.println("arraySum([]) = " + arraySum(new int[]{}));
    }
}
