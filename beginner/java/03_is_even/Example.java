/**
 * Challenge 03: Is Even
 * This file contains a working example solution.
 * Study it, then implement your own in Solution.java
 */
public class Example {
    
    /**
     * Determine if a number is even
     * 
     * Key concepts:
     * - boolean type (true/false)
     * - Modulo operator (%)
     * - Comparison operators (==)
     * - Returning boolean expressions
     * 
     * A number is even if dividing by 2 leaves no remainder
     * 
     * @param n The number to check
     * @return true if n is even, false if n is odd
     */
    public static boolean isEven(int n) {
        return n % 2 == 0;
    }
    
    public static void main(String[] args) {
        // Test cases
        int[] testValues = {4, 7, 0, -2, -3};
        
        for (int val : testValues) {
            System.out.println("isEven(" + val + ") = " + isEven(val));
        }
        
        // Explanation
        System.out.println("\nHow it works:");
        System.out.println("- n % 2: remainder when dividing by 2");
        System.out.println("- == 0: checks if remainder is 0");
        System.out.println("- boolean: true or false");
        System.out.println("\nExamples:");
        System.out.println("- 4 % 2 = 0, so even (returns true)");
        System.out.println("- 7 % 2 = 1, so odd (returns false)");
    }
}
