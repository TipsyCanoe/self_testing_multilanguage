/**
 * Challenge 10: Exception Handling - Safe Divide
 * TODO: Implement the safeDivide method with exception handling
 */
public class Solution {
    
    /**
     * Safely divide two integers with exception handling
     * 
     * @param a The dividend
     * @param b The divisor
     * @return The result of a/b, or 0 if division by zero
     */
    public static int safeDivide(int a, int b) {
        try {
            return a / b;
        } catch (ArithmeticException e) {
            // Handle division by zero
            return 0;
        }
    }
    
    public static void main(String[] args) {
        // Test your method
        System.out.println("safeDivide(10, 2) = " + safeDivide(10, 2));
        System.out.println("safeDivide(10, 3) = " + safeDivide(10, 3));
        System.out.println("safeDivide(10, 0) = " + safeDivide(10, 0));
        System.out.println("safeDivide(0, 5) = " + safeDivide(0, 5));
    }
}
