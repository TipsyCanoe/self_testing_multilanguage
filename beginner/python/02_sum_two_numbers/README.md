# Challenge 02: Sum Two Numbers

**Difficulty**: Beginner  
**Language**: Python  
**Topics**: Functions, Arithmetic, Parameters

## Description

Write a function that takes two numbers and returns their sum.

## Requirements

- Create a function `sum_two(a, b)` that returns the sum of a and b
- Handle integers and floats
- Handle negative numbers

## Function Signature

```python
def sum_two(a: float, b: float) -> float:
    pass
```

## Examples

```python
sum_two(5, 3) → 8
sum_two(-2, 7) → 5
sum_two(0.5, 0.3) → 0.8
sum_two(-5, -3) → -8
```

## Skills Practiced

- Function parameters
- Return values
- Basic arithmetic
- Type hints

## Testing

Run tests with:
```bash
pytest ../../tests/python/test_02_sum_two_numbers.py -v
```
