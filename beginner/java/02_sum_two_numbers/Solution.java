/**
 * Challenge 02: Sum Two Numbers
 * TODO: Implement the sum method
 */
public class Solution {
    
    /**
     * Calculate the sum of two integers
     * 
     * @param a First integer
     * @param b Second integer
     * @return The sum of a and b
     */
    public static int sum(int a, int b) {
        return a + b;
        
    }
    
    public static void main(String[] args) {
        // Test your method
        System.out.println("sum(5, 3) = " + sum(5, 3));
        System.out.println("sum(-2, 7) = " + sum(-2, 7));
        System.out.println("sum(0, 0) = " + sum(0, 0));
    }
}
