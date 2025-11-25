# Challenge 10: Simple Struct - Point

**Difficulty**: Beginner  
**Language**: C  
**Topics**: Structs, Functions with structs, Basic geometry

## Description

Create a struct to represent a 2D point and write functions to work with it.

## Requirements

1. Define a struct `Point` with two integer fields: `x` and `y`
2. Create a function `Point create_point(int x, int y)` that returns a Point
3. Create a function `double distance_from_origin(Point p)` that calculates the distance from (0,0)

## Function Signatures

```c
typedef struct {
    int x;
    int y;
} Point;

Point create_point(int x, int y);
double distance_from_origin(Point p);
```

## Examples

```c
Point p1 = create_point(3, 4);
distance_from_origin(p1) → 5.0

Point p2 = create_point(0, 0);
distance_from_origin(p2) → 0.0

Point p3 = create_point(-3, -4);
distance_from_origin(p3) → 5.0
```

## Mathematical Formula

Distance from origin: √(x² + y²)

## Skills Practiced

- Struct definition
- Working with struct members
- Returning structs from functions
- Mathematical operations (sqrt, pow)
- Using math.h library

## Testing

Your solution will be tested with:
- Positive coordinates
- Negative coordinates
- Origin (0, 0)
- Various distances
