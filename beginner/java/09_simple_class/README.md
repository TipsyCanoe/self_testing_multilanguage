# Challenge 09: Simple Class - Rectangle

**Difficulty**: Beginner  
**Language**: Java  
**Topics**: Classes, Objects, Methods, OOP

## Description

Create a Rectangle class with basic properties and methods.

## Requirements

1. Create a class `Rectangle` with private fields: `width` and `height` (both double)
2. Create a constructor that takes width and height
3. Create getter methods: `getWidth()` and `getHeight()`
4. Create a method `area()` that returns the area (width × height)
5. Create a method `perimeter()` that returns the perimeter (2 × (width + height))

## Class Structure

```java
public class Rectangle {
    private double width;
    private double height;
    
    public Rectangle(double width, double height) { }
    public double getWidth() { }
    public double getHeight() { }
    public double area() { }
    public double perimeter() { }
}
```

## Examples

```java
Rectangle r = new Rectangle(5.0, 3.0);
r.getWidth() → 5.0
r.getHeight() → 3.0
r.area() → 15.0
r.perimeter() → 16.0
```

## Skills Practiced

- Class definition
- Constructor
- Private fields
- Getter methods
- Instance methods
- Basic OOP concepts

## Testing

Run tests with:
```bash
mvn test -Dtest=RectangleTest
```
