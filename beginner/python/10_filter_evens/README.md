# Challenge 10: List Comprehension - Filter Evens

**Difficulty**: Beginner  
**Language**: Python  
**Topics**: List comprehension, Filtering

## Description

Write a function that returns only the even numbers from a list.

## Requirements

- Create a function `filter_evens(numbers)` that returns a list of even numbers
- Preserve the original order
- Use list comprehension (bonus) or any method you prefer

## Function Signature

```python
def filter_evens(numbers: list) -> list:
    pass
```

## Examples

```python
filter_evens([1, 2, 3, 4, 5, 6]) → [2, 4, 6]
filter_evens([1, 3, 5, 7]) → []
filter_evens([2, 4, 6, 8]) → [2, 4, 6, 8]
filter_evens([]) → []
filter_evens([-2, -1, 0, 1, 2]) → [-2, 0, 2]
```

## Skills Practiced

- List comprehension (optional)
- Filtering data
- Even/odd checking
- List operations

## Testing

Run tests with:
```bash
pytest ../../tests/python/test_10_filter_evens.py -v
```
