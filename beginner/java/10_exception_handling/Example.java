/**
 * Challenge 10: Exception Handling - Safe Divide
 * This file contains a working example solution.
 * Study it, then implement your own in Solution.java
 */
public class Example {
    
    /**
     * Safely divide two integers with exception handling
     * 
     * Key concepts:
     * - try-catch blocks
     * - ArithmeticException
     * - Error handling
     * - Defensive programming
     * 
     * Division by zero throws ArithmeticException in Java
     * We catch it and return 0 instead
     * 
     * @param a The dividend
     * @param b The divisor
     * @return The result of a/b, or 0 if division by zero
     */
    public static int safeDivide(int a, int b) {
        try {
            // Try to perform division
            return a / b;
        } catch (ArithmeticException e) {
            // Handle division by zero
            return 0;
        }
    }
    
    public static void main(String[] args) {
        // Test cases
        System.out.println("safeDivide(10, 2) = " + safeDivide(10, 2));
        System.out.println("safeDivide(10, 3) = " + safeDivide(10, 3));
        System.out.println("safeDivide(10, 0) = " + safeDivide(10, 0) + " (caught exception!)");
        System.out.println("safeDivide(0, 5) = " + safeDivide(0, 5));
        
        // Explanation
        System.out.println("\nException Handling:");
        System.out.println("try {");
        System.out.println("    // Code that might throw exception");
        System.out.println("    return a / b;");
        System.out.println("} catch (ArithmeticException e) {");
        System.out.println("    // Handle the error");
        System.out.println("    return 0;");
        System.out.println("}");
        System.out.println("\nWhat happens:");
        System.out.println("1. Try to divide");
        System.out.println("2. If b=0, ArithmeticException is thrown");
        System.out.println("3. catch block handles it");
        System.out.println("4. Return 0 instead of crashing");
        
        // Demonstrate without try-catch (commented to prevent crash)
        System.out.println("\nWithout try-catch, 10/0 would crash the program!");
        // System.out.println(10 / 0); // This would throw ArithmeticException
    }
}
