# Challenge 05: Array Sum

**Difficulty**: Beginner  
**Language**: C  
**Topics**: Arrays, Loops, Accumulation

## Description

Write a function that calculates the sum of all elements in an integer array.

## Requirements

- Create a function `int array_sum(int arr[], int size)` that returns the sum of all elements
- Handle empty arrays (size = 0, should return 0)
- Handle negative numbers

## Function Signature

```c
int array_sum(int arr[], int size);
```

## Examples

```c
int arr1[] = {1, 2, 3, 4, 5};
array_sum(arr1, 5) → 15

int arr2[] = {-1, -2, -3};
array_sum(arr2, 3) → -6

int arr3[] = {10};
array_sum(arr3, 1) → 10

int arr4[] = {};
array_sum(arr4, 0) → 0
```

## Skills Practiced

- Array traversal
- Loop iteration
- Accumulator pattern
- Working with array size parameter

## Testing

Your solution will be tested with:
- Normal arrays
- Arrays with negative numbers
- Single-element arrays
- Empty arrays
- Large arrays
