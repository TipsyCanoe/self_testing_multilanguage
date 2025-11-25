# Challenge 02: Sum Two Numbers

**Difficulty**: Beginner  
**Language**: Java  
**Topics**: Methods, Parameters, Arithmetic

## Description

Write a Java method that takes two integers and returns their sum.

## Requirements

- Create a method `sum(int a, int b)` that returns the sum of a and b
- Handle positive and negative numbers
- Method should be static and public

## Method Signature

```java
public static int sum(int a, int b)
```

## Examples

```java
sum(5, 3) → 8
sum(-2, 7) → 5
sum(0, 0) → 0
sum(-5, -3) → -8
```

## Skills Practiced

- Method parameters
- Return values
- Integer arithmetic
- Basic math operations

## Testing

Run tests with:
```bash
mvn test -Dtest=SumTwoNumbersTest
```
