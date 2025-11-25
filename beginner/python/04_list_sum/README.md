# Challenge 04: List Sum

**Difficulty**: Beginner  
**Language**: Python  
**Topics**: Lists, Loops, Accumulation

## Description

Write a function that calculates the sum of all numbers in a list.

## Requirements

- Create a function `list_sum(numbers)` that returns the sum of all elements
- Handle empty lists (return 0)
- Handle negative numbers

## Function Signature

```python
def list_sum(numbers: list) -> float:
    pass
```

## Examples

```python
list_sum([1, 2, 3, 4, 5]) → 15
list_sum([-1, -2, -3]) → -6
list_sum([10]) → 10
list_sum([]) → 0
list_sum([1.5, 2.5, 3.0]) → 7.0
```

## Skills Practiced

- List iteration
- Accumulator pattern
- Handling empty lists
- Working with numeric data

## Testing

Run tests with:
```bash
pytest ../../tests/python/test_04_list_sum.py -v
```
