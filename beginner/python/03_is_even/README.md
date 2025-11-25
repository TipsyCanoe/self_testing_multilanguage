# Challenge 03: Is Even

**Difficulty**: Beginner  
**Language**: Python  
**Topics**: Conditionals, Modulo operator, Boolean

## Description

Write a function that determines if a number is even.

## Requirements

- Create a function `is_even(n)` that returns True if n is even, False otherwise
- Use the modulo operator (%)

## Function Signature

```python
def is_even(n: int) -> bool:
    pass
```

## Examples

```python
is_even(4) → True
is_even(7) → False
is_even(0) → True
is_even(-2) → True
is_even(-3) → False
```

## Skills Practiced

- Boolean logic
- Modulo operator
- Conditional expressions
- Even/odd determination

## Testing

Run tests with:
```bash
pytest ../../tests/python/test_03_is_even.py -v
```
