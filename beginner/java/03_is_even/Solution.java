/**
 * Challenge 03: Is Even
 * TODO: Implement the isEven method
 */
public class Solution {
    
    /**
     * Determine if a number is even
     * 
     * @param n The number to check
     * @return true if n is even, false if n is odd
     */
    public static boolean isEven(int n) {
        return n % 2 == 0;
    }
    
    public static void main(String[] args) {
        // Test your method
        System.out.println("isEven(4) = " + isEven(4));
        System.out.println("isEven(7) = " + isEven(7));
        System.out.println("isEven(0) = " + isEven(0));
        System.out.println("isEven(-2) = " + isEven(-2));
    }
}
