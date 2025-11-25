# Challenge 04: Array Sum

**Difficulty**: Beginner  
**Language**: Java  
**Topics**: Arrays, Loops, Accumulation

## Description

Write a Java method that calculates the sum of all elements in an integer array.

## Requirements

- Create a method `arraySum(int[] arr)` that returns the sum of all elements
- Handle empty arrays (return 0)
- Handle negative numbers

## Method Signature

```java
public static int arraySum(int[] arr)
```

## Examples

```java
arraySum(new int[]{1, 2, 3, 4, 5}) → 15
arraySum(new int[]{-1, -2, -3}) → -6
arraySum(new int[]{10}) → 10
arraySum(new int[]{}) → 0
```

## Skills Practiced

- Array traversal
- For loops
- Accumulator pattern
- Working with arrays

## Testing

Run tests with:
```bash
mvn test -Dtest=ArraySumTest
```
