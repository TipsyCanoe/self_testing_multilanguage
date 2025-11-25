/**
 * Challenge 06: Count Vowels
 * This file contains a working example solution.
 * Study it, then implement your own in Solution.java
 */
public class Example {
    
    /**
     * Count the number of vowels in a string
     * 
     * Key concepts:
     * - String traversal
     * - charAt() method
     * - String contains() or indexOf()
     * - Character checking
     * - Case-insensitive comparison
     * 
     * @param text A string to analyze
     * @return The number of vowels (a, e, i, o, u, A, E, I, O, U)
     */
    public static int countVowels(String text) {
        // Define vowels
        String vowels = "aeiouAEIOU";
        int count = 0;
        
        // Check each character
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (vowels.indexOf(c) != -1) {
                count++;
            }
        }
        
        return count;
        
        // Alternative approach:
        // for (char c : text.toCharArray()) {
        //     if ("aeiouAEIOU".contains(String.valueOf(c))) {
        //         count++;
        //     }
        // }
    }
    
    public static void main(String[] args) {
        // Test cases
        String[] tests = {"hello", "AEIOU", "xyz", "Programming"};
        
        for (String test : tests) {
            System.out.println("countVowels(\"" + test + "\") = " + countVowels(test));
        }
        
        // Explanation
        System.out.println("\nKey methods:");
        System.out.println("- text.length(): get string length");
        System.out.println("- text.charAt(i): get character at index");
        System.out.println("- indexOf(c): find character in string (-1 if not found)");
        System.out.println("\nExample: \"hello\"");
        System.out.println("  h - not in vowels");
        System.out.println("  e - vowel! count = 1");
        System.out.println("  l - not in vowels");
        System.out.println("  l - not in vowels");
        System.out.println("  o - vowel! count = 2");
    }
}
