/**
 * Challenge 02: Sum Two Numbers
 * This file contains a working example solution.
 * Study it, then implement your own in Solution.java
 */
public class Example {
    
    /**
     * Calculate the sum of two integers
     * 
     * Key concepts:
     * - Method parameters
     * - Return values
     * - Integer arithmetic
     * - Type declarations
     * 
     * @param a First integer
     * @param b Second integer
     * @return The sum of a and b
     */
    public static int sum(int a, int b) {
        return a + b;
    }
    
    public static void main(String[] args) {
        // Test cases
        System.out.println("sum(5, 3) = " + sum(5, 3));
        System.out.println("sum(-2, 7) = " + sum(-2, 7));
        System.out.println("sum(0, 0) = " + sum(0, 0));
        System.out.println("sum(-5, -3) = " + sum(-5, -3));
        
        // Explanation
        System.out.println("\nKey concepts:");
        System.out.println("- int: integer type in Java");
        System.out.println("- Parameters declared with type: int a");
        System.out.println("- Return type matches declaration");
        System.out.println("- + operator for addition");
    }
}
