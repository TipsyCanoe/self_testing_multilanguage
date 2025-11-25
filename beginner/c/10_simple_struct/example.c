#include <stdio.h>
#include <math.h>

/**
 * Challenge 10: Simple Struct - Point
 * This file contains a working example solution.
 * Study it, then implement your own in solution.c
 */

/**
 * Define the Point struct
 * 
 * Key concepts:
 * - Struct definition
 * - typedef for convenience
 * - Struct members (fields)
 */
typedef struct {
    int x;
    int y;
} Point;

/**
 * Create a Point with the given x and y coordinates
 * 
 * @param x The x-coordinate
 * @param y The y-coordinate
 * @return A Point struct with the given coordinates
 */
Point create_point(int x, int y) {
    Point p;
    p.x = x;
    p.y = y;
    return p;
}

/**
 * Calculate the distance of a point from the origin (0, 0)
 * 
 * @param p The point
 * @return The distance from origin (sqrt(x^2 + y^2))
 * 
 * Formula: distance = √(x² + y²)
 * Example: Point (3, 4) → √(9 + 16) = √25 = 5
 */
double distance_from_origin(Point p) {
    // Use Pythagorean theorem
    // sqrt and pow are from math.h
    return sqrt(pow(p.x, 2) + pow(p.y, 2));
}

int main() {
    // Test case 1
    Point p1 = create_point(3, 4);
    printf("Point (3, 4):\n");
    printf("  x = %d, y = %d\n", p1.x, p1.y);
    printf("  distance = %.2f\n\n", distance_from_origin(p1));
    
    // Test case 2
    Point p2 = create_point(0, 0);
    printf("Point (0, 0):\n");
    printf("  distance = %.2f\n\n", distance_from_origin(p2));
    
    // Test case 3
    Point p3 = create_point(-3, -4);
    printf("Point (-3, -4):\n");
    printf("  distance = %.2f\n\n", distance_from_origin(p3));
    
    // Explanation
    printf("How it works:\n");
    printf("1. Struct holds two integers: x and y\n");
    printf("2. create_point() returns a Point struct\n");
    printf("3. distance_from_origin() uses Pythagorean theorem\n");
    printf("4. Formula: d = √(x² + y²)\n");
    printf("\nExample: Point (3, 4)\n");
    printf("  x² = 3² = 9\n");
    printf("  y² = 4² = 16\n");
    printf("  x² + y² = 25\n");
    printf("  √25 = 5\n");
    printf("\nCompile with: gcc example.c -o example -lm\n");
    printf("(The -lm flag links the math library)\n");
    
    return 0;
}
