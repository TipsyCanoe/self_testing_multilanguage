/**
 * Challenge 01: Hello World
 * This file contains a working example solution.
 * Study it, then implement your own in Solution.java
 */
public class Example {
    
    /**
     * Return the string "Hello, World!"
     * 
     * Key concepts:
     * - Static methods (can be called without creating object)
     * - Return type (String)
     * - Method naming conventions (camelCase)
     * 
     * @return The string "Hello, World!"
     */
    public static String helloWorld() {
        return "Hello, World!";
    }
    
    public static void main(String[] args) {
        // Test the method
        String result = helloWorld();
        System.out.println(result);
        
        // Additional info
        System.out.println("\nBreakdown:");
        System.out.println("- public: accessible from anywhere");
        System.out.println("- static: belongs to class, not instance");
        System.out.println("- String: return type");
        System.out.println("- return: sends value back to caller");
    }
}
