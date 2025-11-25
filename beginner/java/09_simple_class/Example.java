/**
 * Challenge 09: Simple Class - Rectangle
 * This file contains a working example solution.
 * Study it, then implement your own in Rectangle.java
 */
public class Example {
    // Private fields (data encapsulation)
    private double width;
    private double height;
    
    /**
     * Constructor
     * 
     * Key concepts:
     * - Constructor has same name as class
     * - No return type (not even void)
     * - Initializes object state
     * - 'this' refers to current object
     * 
     * @param width The width of the rectangle
     * @param height The height of the rectangle
     */
    public Example(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    /**
     * Get the width
     * 
     * Getter methods provide controlled access to private fields
     * 
     * @return The width
     */
    public double getWidth() {
        return width;
    }
    
    /**
     * Get the height
     * @return The height
     */
    public double getHeight() {
        return height;
    }
    
    /**
     * Calculate the area
     * 
     * Instance methods can access object's fields
     * 
     * @return The area (width × height)
     */
    public double area() {
        return width * height;
    }
    
    /**
     * Calculate the perimeter
     * @return The perimeter (2 × (width + height))
     */
    public double perimeter() {
        return 2 * (width + height);
    }
    
    public static void main(String[] args) {
        // Create a rectangle object
        Example rect = new Example(5.0, 3.0);
        
        // Test methods
        System.out.println("Width: " + rect.getWidth());
        System.out.println("Height: " + rect.getHeight());
        System.out.println("Area: " + rect.area());
        System.out.println("Perimeter: " + rect.perimeter());
        
        // Explanation
        System.out.println("\nOOP Concepts:");
        System.out.println("- Class: blueprint (Example)");
        System.out.println("- Object: instance (rect)");
        System.out.println("- Fields: data (width, height)");
        System.out.println("- Methods: behavior (area, perimeter)");
        System.out.println("- Constructor: initialization");
        System.out.println("- Encapsulation: private fields, public methods");
    }
}
