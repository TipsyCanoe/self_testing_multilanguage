# Challenge 06: Count Vowels

**Difficulty**: Beginner  
**Language**: Java  
**Topics**: Strings, Character comparison, Loops

## Description

Write a Java method that counts the number of vowels in a string.

## Requirements

- Create a method `countVowels(String text)` that returns the count of vowels
- Count both uppercase and lowercase vowels
- Vowels are: A, E, I, O, U, a, e, i, o, u

## Method Signature

```java
public static int countVowels(String text)
```

## Examples

```java
countVowels("hello") → 2
countVowels("AEIOU") → 5
countVowels("xyz") → 0
countVowels("") → 0
countVowels("Programming") → 3
```

## Skills Practiced

- String traversal
- Character comparison
- Case-insensitive checking
- Counting pattern

## Testing

Run tests with:
```bash
mvn test -Dtest=CountVowelsTest
```
