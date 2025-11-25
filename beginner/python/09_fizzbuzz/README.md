# Challenge 09: FizzBuzz

**Difficulty**: Beginner  
**Language**: Python  
**Topics**: Conditionals, Loops, Modulo

## Description

Write a function that returns a list of FizzBuzz values for numbers 1 to n.

## Requirements

- Create a function `fizzbuzz(n)` that returns a list
- For each number from 1 to n:
  - If divisible by 3 and 5: append "FizzBuzz"
  - If divisible by 3: append "Fizz"
  - If divisible by 5: append "Buzz"
  - Otherwise: append the number itself

## Function Signature

```python
def fizzbuzz(n: int) -> list:
    pass
```

## Examples

```python
fizzbuzz(5) → [1, 2, "Fizz", 4, "Buzz"]
fizzbuzz(15) → [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
fizzbuzz(1) → [1]
```

## Skills Practiced

- Conditional logic
- Modulo operator
- List building
- Classic programming problem

## Testing

Run tests with:
```bash
pytest ../../tests/python/test_09_fizzbuzz.py -v
```
