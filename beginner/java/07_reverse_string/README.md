# Challenge 07: Reverse String

**Difficulty**: Beginner  
**Language**: Java  
**Topics**: Strings, StringBuilder, Reversal

## Description

Write a Java method that reverses a string.

## Requirements

- Create a method `reverseString(String text)` that returns the reversed string
- Handle empty strings
- You can use StringBuilder or any method you prefer

## Method Signature

```java
public static String reverseString(String text)
```

## Examples

```java
reverseString("hello") → "olleh"
reverseString("Java") → "avaJ"
reverseString("") → ""
reverseString("a") → "a"
reverseString("12345") → "54321"
```

## Skills Practiced

- String manipulation
- StringBuilder usage (optional)
- String reversal techniques

## Testing

Run tests with:
```bash
mvn test -Dtest=ReverseStringTest
```
