# Challenge 10: Exception Handling

**Difficulty**: Beginner  
**Language**: Java  
**Topics**: Exceptions, Try-catch, Error handling

## Description

Write a Java method that safely divides two numbers with exception handling.

## Requirements

- Create a method `safeDivide(int a, int b)` that returns the result of a/b
- Handle division by zero by catching ArithmeticException
- Return 0 if division by zero occurs
- Method should be static and public

## Method Signature

```java
public static int safeDivide(int a, int b)
```

## Examples

```java
safeDivide(10, 2) → 5
safeDivide(10, 3) → 3 (integer division)
safeDivide(10, 0) → 0 (exception caught)
safeDivide(0, 5) → 0
```

## Skills Practiced

- Exception handling
- Try-catch blocks
- ArithmeticException
- Safe operations
- Error handling patterns

## Testing

Run tests with:
```bash
mvn test -Dtest=SafeDivideTest
```
