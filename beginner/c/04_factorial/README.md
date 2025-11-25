# Challenge 04: Factorial

**Difficulty**: Beginner  
**Language**: C  
**Topics**: Loops, Iteration, Multiplication

## Description

Write a function that calculates the factorial of a non-negative integer.

## Requirements

- Create a function `long factorial(int n)` that returns n! (n factorial)
- Handle n = 0 (0! = 1)
- Assume n will be non-negative and small enough to fit in a long

## Function Signature

```c
long factorial(int n);
```

## Examples

```c
factorial(0) → 1
factorial(1) → 1
factorial(5) → 120
factorial(10) → 3628800
```

## Mathematical Definition

- 0! = 1
- n! = n × (n-1) × (n-2) × ... × 2 × 1

## Skills Practiced

- For loops or while loops
- Accumulator pattern
- Mathematical operations
- Edge case handling (0!)

## Testing

Your solution will be tested with:
- Edge case: 0
- Small values: 1-5
- Larger values: 10, 12
