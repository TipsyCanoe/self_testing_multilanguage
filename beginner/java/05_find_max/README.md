# Challenge 05: Find Maximum

**Difficulty**: Beginner  
**Language**: Java  
**Topics**: Arrays, Comparison, Logic

## Description

Write a Java method that finds the maximum value in an integer array.

## Requirements

- Create a method `findMax(int[] arr)` that returns the maximum value
- Assume the array has at least one element
- Handle negative numbers

## Method Signature

```java
public static int findMax(int[] arr)
```

## Examples

```java
findMax(new int[]{3, 7, 2, 9, 1}) → 9
findMax(new int[]{-5, -2, -10, -1}) → -1
findMax(new int[]{42}) → 42
findMax(new int[]{5, 5, 5, 5}) → 5
```

## Skills Practiced

- Array traversal
- Comparison operators
- Tracking maximum value
- Conditional logic

## Testing

Run tests with:
```bash
mvn test -Dtest=FindMaxTest
```
