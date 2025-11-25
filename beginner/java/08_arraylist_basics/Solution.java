import java.util.ArrayList;

/**
 * Challenge 08: ArrayList Basics - Filter Evens
 * TODO: Implement the filterEvens method
 */
public class Solution {
    
    /**
     * Filter and return only the even numbers from an ArrayList
     * 
     * @param numbers An ArrayList of integers
     * @return An ArrayList containing only the even numbers
     */
    public static ArrayList<Integer> filterEvens(ArrayList<Integer> numbers) {
        ArrayList<Integer> result = new ArrayList<>();
        for (Integer num : numbers) {
            if (num % 2 == 0) {
                result.add(num);
            }
        }
        return result;
    }
    
    public static void main(String[] args) {
        // Test your method
        ArrayList<Integer> list1 = new ArrayList<>();
        list1.add(1); list1.add(2); list1.add(3); list1.add(4); list1.add(5); list1.add(6);
        System.out.println("filterEvens([1,2,3,4,5,6]) = " + filterEvens(list1));
        
        ArrayList<Integer> list2 = new ArrayList<>();
        list2.add(1); list2.add(3); list2.add(5); list2.add(7);
        System.out.println("filterEvens([1,3,5,7]) = " + filterEvens(list2));
    }
}
