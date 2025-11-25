# Challenge 08: Dictionary Basics

**Difficulty**: Beginner  
**Language**: Python  
**Topics**: Dictionaries, Key-value pairs

## Description

Write a function that counts the frequency of each character in a string.

## Requirements

- Create a function `char_frequency(text)` that returns a dictionary
- Keys are characters, values are their frequencies
- Ignore case (treat 'A' and 'a' as the same)
- Include spaces and punctuation

## Function Signature

```python
def char_frequency(text: str) -> dict:
    pass
```

## Examples

```python
char_frequency("hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
char_frequency("aaa") → {'a': 3}
char_frequency("") → {}
char_frequency("Hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

## Skills Practiced

- Dictionary creation and manipulation
- Character counting
- Case normalization
- Key-value operations

## Testing

Run tests with:
```bash
pytest ../../tests/python/test_08_char_frequency.py -v
```
