# Challenge 08: ArrayList Basics

**Difficulty**: Beginner  
**Language**: Java  
**Topics**: ArrayList, Collections, Filtering

## Description

Write a Java method that returns only the even numbers from an ArrayList.

## Requirements

- Create a method `filterEvens(ArrayList<Integer> numbers)` that returns an ArrayList of even numbers
- Preserve the original order
- Use ArrayList operations

## Method Signature

```java
public static ArrayList<Integer> filterEvens(ArrayList<Integer> numbers)
```

## Examples

```java
filterEvens([1, 2, 3, 4, 5, 6]) → [2, 4, 6]
filterEvens([1, 3, 5, 7]) → []
filterEvens([2, 4, 6, 8]) → [2, 4, 6, 8]
filterEvens([]) → []
filterEvens([-2, -1, 0, 1, 2]) → [-2, 0, 2]
```

## Skills Practiced

- ArrayList operations
- Filtering data
- Even/odd checking
- Collections manipulation

## Testing

Run tests with:
```bash
mvn test -Dtest=FilterEvensTest
```
