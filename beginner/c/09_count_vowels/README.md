# Challenge 09: Count Vowels

**Difficulty**: Beginner  
**Language**: C  
**Topics**: Strings, Character comparison, Conditionals

## Description

Write a function that counts the number of vowels (a, e, i, o, u) in a string.

## Requirements

- Create a function `int count_vowels(const char *str)` that returns the count of vowels
- Count both uppercase and lowercase vowels
- Vowels are: A, E, I, O, U, a, e, i, o, u

## Function Signature

```c
int count_vowels(const char *str);
```

## Examples

```c
count_vowels("hello") → 2
count_vowels("AEIOU") → 5
count_vowels("xyz") → 0
count_vowels("") → 0
count_vowels("Programming") → 3
count_vowels("bcdfg") → 0
```

## Skills Practiced

- String traversal
- Character comparison
- Case-insensitive checking
- Conditional logic

## Testing

Your solution will be tested with:
- Strings with lowercase vowels
- Strings with uppercase vowels
- Strings with mixed case
- Strings with no vowels
- Empty strings
