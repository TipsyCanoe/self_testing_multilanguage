# Challenge 05: Find Maximum

**Difficulty**: Beginner  
**Language**: Python  
**Topics**: Lists, Comparison, Logic

## Description

Write a function that finds the maximum value in a list WITHOUT using the built-in max() function.

## Requirements

- Create a function `find_max(numbers)` that returns the maximum value
- Do NOT use the built-in max() function
- Assume the list has at least one element
- Handle negative numbers

## Function Signature

```python
def find_max(numbers: list) -> float:
    pass
```

## Examples

```python
find_max([3, 7, 2, 9, 1]) → 9
find_max([-5, -2, -10, -1]) → -1
find_max([42]) → 42
find_max([5.5, 2.3, 8.1]) → 8.1
```

## Skills Practiced

- List traversal
- Comparison operators
- Tracking maximum value
- Conditional logic

## Testing

Run tests with:
```bash
pytest ../../tests/python/test_05_find_max.py -v
```
