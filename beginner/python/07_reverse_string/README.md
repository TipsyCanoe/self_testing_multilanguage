# Challenge 07: Reverse String

**Difficulty**: Beginner  
**Language**: Python  
**Topics**: Strings, Slicing, Reversal

## Description

Write a function that reverses a string.

## Requirements

- Create a function `reverse_string(text)` that returns the reversed string
- Handle empty strings
- You can use Python string slicing or any method you prefer

## Function Signature

```python
def reverse_string(text: str) -> str:
    pass
```

## Examples

```python
reverse_string("hello") → "olleh"
reverse_string("Python") → "nohtyP"
reverse_string("") → ""
reverse_string("a") → "a"
reverse_string("12345") → "54321"
```

## Skills Practiced

- String manipulation
- String slicing (optional)
- String reversal techniques

## Testing

Run tests with:
```bash
pytest ../../tests/python/test_07_reverse_string.py -v
```
