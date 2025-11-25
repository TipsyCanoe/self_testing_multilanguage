# Challenge 08: Reverse Array

**Difficulty**: Beginner  
**Language**: C  
**Topics**: Arrays, In-place modification, Two pointers

## Description

Write a function that reverses an integer array in-place.

## Requirements

- Create a function `void reverse_array(int arr[], int size)` that reverses the array
- Modify the array in-place (do not create a new array)
- Handle arrays of any size including empty arrays

## Function Signature

```c
void reverse_array(int arr[], int size);
```

## Examples

```c
int arr1[] = {1, 2, 3, 4, 5};
reverse_array(arr1, 5);
// arr1 is now {5, 4, 3, 2, 1}

int arr2[] = {10, 20};
reverse_array(arr2, 2);
// arr2 is now {20, 10}

int arr3[] = {42};
reverse_array(arr3, 1);
// arr3 is still {42}
```

## Skills Practiced

- In-place array manipulation
- Two-pointer technique
- Swapping elements
- Array indexing

## Testing

Your solution will be tested with:
- Arrays with odd number of elements
- Arrays with even number of elements
- Single-element arrays
- Empty arrays
- Already reversed arrays
