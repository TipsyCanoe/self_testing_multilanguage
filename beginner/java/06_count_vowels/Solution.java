import java.util.Arrays;

/**
 * Challenge 06: Count Vowels
 * TODO: Implement the countVowels method
 */
public class Solution {
    
    /**
     * Count the number of vowels in a string
     * 
     * @param text A string to analyze
     * @return The number of vowels (a, e, i, o, u, A, E, I, O, U)
     */
    public static int countVowels(String text) {
        int restult = 0;
        Character[] vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (Arrays.asList(vowels).contains(c)) {
                restult++;
            }
        }
        return restult;
    }
    
    public static void main(String[] args) {
        // Test your method
        System.out.println("countVowels(\"hello\") = " + countVowels("hello"));
        System.out.println("countVowels(\"AEIOU\") = " + countVowels("AEIOU"));
        System.out.println("countVowels(\"xyz\") = " + countVowels("xyz"));
        System.out.println("countVowels(\"Programming\") = " + countVowels("Programming"));
    }
}
