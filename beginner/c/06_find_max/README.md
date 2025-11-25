# Challenge 06: Find Maximum

**Difficulty**: Beginner  
**Language**: C  
**Topics**: Arrays, Comparison, Logic

## Description

Write a function that finds the maximum value in an integer array.

## Requirements

- Create a function `int find_max(int arr[], int size)` that returns the maximum value
- Assume the array has at least one element (size >= 1)
- Handle negative numbers

## Function Signature

```c
int find_max(int arr[], int size);
```

## Examples

```c
int arr1[] = {3, 7, 2, 9, 1};
find_max(arr1, 5) → 9

int arr2[] = {-5, -2, -10, -1};
find_max(arr2, 4) → -1

int arr3[] = {42};
find_max(arr3, 1) → 42

int arr4[] = {5, 5, 5, 5};
find_max(arr4, 4) → 5
```

## Skills Practiced

- Array traversal
- Comparison operators
- Tracking maximum value
- Conditional logic

## Testing

Your solution will be tested with:
- Arrays with positive numbers
- Arrays with negative numbers
- Single-element arrays
- Arrays with duplicate maximum values
- Unsorted arrays
