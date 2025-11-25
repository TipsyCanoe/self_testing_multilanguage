# Challenge 07: String Length

**Difficulty**: Beginner  
**Language**: C  
**Topics**: Strings, Pointers, Null terminator

## Description

Write a function that calculates the length of a string WITHOUT using the built-in strlen() function.

## Requirements

- Create a function `int string_length(const char *str)` that returns the length of the string
- Do NOT use strlen() or any other string library functions
- Count characters until the null terminator '\0'

## Function Signature

```c
int string_length(const char *str);
```

## Examples

```c
string_length("hello") → 5
string_length("") → 0
string_length("C programming") → 13
string_length("a") → 1
```

## Skills Practiced

- String representation in C
- Null terminator concept
- Pointer arithmetic or array indexing
- Character counting

## Testing

Your solution will be tested with:
- Normal strings
- Empty string
- Single character string
- Strings with spaces
- Long strings
