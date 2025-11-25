# Challenge 03: Is Even

**Difficulty**: Beginner  
**Language**: Java  
**Topics**: Conditionals, Modulo operator, Boolean

## Description

Write a Java method that determines if a number is even.

## Requirements

- Create a method `isEven(int n)` that returns true if n is even, false otherwise
- Use the modulo operator (%)
- Method should be static and public

## Method Signature

```java
public static boolean isEven(int n)
```

## Examples

```java
isEven(4) → true
isEven(7) → false
isEven(0) → true
isEven(-2) → true
isEven(-3) → false
```

## Skills Practiced

- Boolean return type
- Modulo operator
- Conditional logic
- Even/odd determination

## Testing

Run tests with:
```bash
mvn test -Dtest=IsEvenTest
```
