/**
 * Challenge 07: Reverse String
 * TODO: Implement the reverseString method
 */
public class Solution {
    
    /**
     * Reverse a string
     * 
     * @param text A string to reverse
     * @return The reversed string
     */
public static String reverseString(String text) {
    if (text == null || text.isEmpty() || text.length() == 1) {
        return text;
    }
    StringBuilder result = new StringBuilder();
    for (int i = text.length() - 1; i >= 0 ; i--) {
        result.append(text.charAt(i));
    }
    return result.toString();
}

    
    public static void main(String[] args) {
        // Test your method
        System.out.println("reverseString(\"hello\") = " + reverseString("hello"));
        System.out.println("reverseString(\"Java\") = " + reverseString("Java"));
        System.out.println("reverseString(\"\") = \"" + reverseString("") + "\"");
    }
}
