/**
 * Challenge 07: Reverse String
 * This file contains a working example solution.
 * Study it, then implement your own in Solution.java
 */
public class Example {
    
    /**
     * Reverse a string
     * 
     * Key concepts:
     * - StringBuilder class
     * - reverse() method
     * - String immutability in Java
     * - Converting between String and StringBuilder
     * 
     * Multiple approaches:
     * 1. StringBuilder with reverse() - most efficient
     * 2. Manual loop building string
     * 3. Recursive approach
     * 
     * @param text A string to reverse
     * @return The reversed string
     */
    public static String reverseString(String text) {
        // Method 1: Using StringBuilder (recommended)
        return new StringBuilder(text).reverse().toString();
        
        // Method 2: Manual loop
        // String result = "";
        // for (int i = text.length() - 1; i >= 0; i--) {
        //     result += text.charAt(i);
        // }
        // return result;
        
        // Method 3: More efficient manual loop
        // StringBuilder sb = new StringBuilder();
        // for (int i = text.length() - 1; i >= 0; i--) {
        //     sb.append(text.charAt(i));
        // }
        // return sb.toString();
    }
    
    public static void main(String[] args) {
        // Test cases
        String[] tests = {"hello", "Java", "", "12345"};
        
        for (String test : tests) {
            System.out.println("reverseString(\"" + test + "\") = \"" + 
                reverseString(test) + "\"");
        }
        
        // Explanation
        System.out.println("\nWhy StringBuilder?");
        System.out.println("- Strings in Java are immutable");
        System.out.println("- StringBuilder is mutable and efficient");
        System.out.println("- reverse() method does it in one call");
        System.out.println("\nSteps:");
        System.out.println("1. Create StringBuilder from string");
        System.out.println("2. Call reverse() method");
        System.out.println("3. Convert back to String with toString()");
    }
}
