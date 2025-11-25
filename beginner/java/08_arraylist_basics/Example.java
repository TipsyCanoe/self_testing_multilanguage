import java.util.ArrayList;

/**
 * Challenge 08: ArrayList Basics - Filter Evens
 * This file contains a working example solution.
 * Study it, then implement your own in Solution.java
 */
public class Example {
    
    /**
     * Filter and return only the even numbers from an ArrayList
     * 
     * Key concepts:
     * - ArrayList (dynamic array)
     * - Generics (ArrayList<Integer>)
     * - add() method
     * - Iterating through ArrayList
     * - Creating and returning new ArrayList
     * 
     * @param numbers An ArrayList of integers
     * @return An ArrayList containing only the even numbers
     */
    public static ArrayList<Integer> filterEvens(ArrayList<Integer> numbers) {
        ArrayList<Integer> evens = new ArrayList<>();
        
        // Check each number
        for (Integer num : numbers) {
            if (num % 2 == 0) {
                evens.add(num);
            }
        }
        
        return evens;
    }
    
    public static void main(String[] args) {
        // Test case 1
        ArrayList<Integer> list1 = new ArrayList<>();
        list1.add(1); list1.add(2); list1.add(3); 
        list1.add(4); list1.add(5); list1.add(6);
        System.out.println("filterEvens([1,2,3,4,5,6]) = " + filterEvens(list1));
        
        // Test case 2
        ArrayList<Integer> list2 = new ArrayList<>();
        list2.add(1); list2.add(3); list2.add(5); list2.add(7);
        System.out.println("filterEvens([1,3,5,7]) = " + filterEvens(list2));
        
        // Test case 3
        ArrayList<Integer> list3 = new ArrayList<>();
        list3.add(-2); list3.add(-1); list3.add(0); 
        list3.add(1); list3.add(2);
        System.out.println("filterEvens([-2,-1,0,1,2]) = " + filterEvens(list3));
        
        // Explanation
        System.out.println("\nArrayList vs Array:");
        System.out.println("- Array: fixed size, use []");
        System.out.println("- ArrayList: dynamic size, use add()");
        System.out.println("\nKey methods:");
        System.out.println("- add(element): add to end");
        System.out.println("- get(index): get element");
        System.out.println("- size(): get number of elements");
    }
}
