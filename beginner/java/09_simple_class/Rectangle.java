/**
 * Challenge 09: Simple Class - Rectangle
 * TODO: Implement the Rectangle class
 */
public class Rectangle {
    double width;
    double height;
    
    /**
     * Constructor
     * @param width The width of the rectangle
     * @param height The height of the rectangle
     */
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    /**
     * Get the width
     * @return The width
     */
    public double getWidth() {
        // Your code here
        return width;
    }
    
    /**
     * Get the height
     * @return The height
     */
    public double getHeight() {
        // Your code here
        return height;
    }
    
    /**
     * Calculate the area
     * @return The area (width × height)
     */
    public double area() {
        // Your code here
        return width * height;
    }
    
    /**
     * Calculate the perimeter
     * @return The perimeter (2 × (width + height))
     */
    public double perimeter() {
        // Your code here
        return 2 * (width + height);
    }
    
    public static void main(String[] args) {
        // Test your class
        Rectangle r = new Rectangle(5.0, 3.0);
        System.out.println("Width: " + r.getWidth());
        System.out.println("Height: " + r.getHeight());
        System.out.println("Area: " + r.area());
        System.out.println("Perimeter: " + r.perimeter());
    }
}
