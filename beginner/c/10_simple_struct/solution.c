#include <stdio.h>
#include <math.h>

/**
 * TODO: Define the Point struct here
 */
typedef struct {
    // Your code here
    int x;
    int y;
} Point;

/**
 * Create a Point with the given x and y coordinates
 * 
 * @param x The x-coordinate
 * @param y The y-coordinate
 * @return A Point struct with the given coordinates
 * 
 * TODO: Implement this function
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
 * TODO: Implement this function
 */
double distance_from_origin(Point p) {
    // Your code here
    int distance = 0.0;
    distance = sqrt(pow(p.x,2) + pow(p.y,2));
    return distance;
}

int main() {
    // Test your functions
    Point p1 = create_point(3, 4);
    printf("Point (3, 4) distance from origin: %.2f\n", distance_from_origin(p1));
    
    Point p2 = create_point(0, 0);
    printf("Point (0, 0) distance from origin: %.2f\n", distance_from_origin(p2));
    
    return 0;
}
