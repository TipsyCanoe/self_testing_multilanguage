# Challenge 06: Count Vowels

**Difficulty**: Beginner  
**Language**: Python  
**Topics**: Strings, Iteration, Conditionals

## Description

Write a function that counts the number of vowels in a string.

## Requirements

- Create a function `count_vowels(text)` that returns the count of vowels
- Count both uppercase and lowercase vowels
- Vowels are: A, E, I, O, U, a, e, i, o, u

## Function Signature

```python
def count_vowels(text: str) -> int:
    pass
```

## Examples

```python
count_vowels("hello") → 2
count_vowels("AEIOU") → 5
count_vowels("xyz") → 0
count_vowels("") → 0
count_vowels("Programming") → 3
```

## Skills Practiced

- String iteration
- Character checking
- Case-insensitive comparison
- Counting pattern

## Testing

Run tests with:
```bash
pytest ../../tests/python/test_06_count_vowels.py -v
```
