/**
 * Challenge 05: Find Maximum
 * TODO: Implement the findMax method
 */
public class Solution {
    
    /**
     * Find the maximum value in an array
     * 
     * @param arr The array of integers (at least one element)
     * @return The maximum value in the array
     */
    public static int findMax(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }
    
    public static void main(String[] args) {
        // Test your method
        System.out.println("findMax([3,7,2,9,1]) = " + findMax(new int[]{3, 7, 2, 9, 1}));
        System.out.println("findMax([-5,-2,-10,-1]) = " + findMax(new int[]{-5, -2, -10, -1}));
        System.out.println("findMax([42]) = " + findMax(new int[]{42}));
    }
}
