# Example Solutions

This file contains example solutions for the first challenge in each language to help you understand the expected format.

## ⚠️ Important Note

These are **example solutions** to show you the expected format and approach. For your learning benefit, try to solve challenges on your own before looking at examples!

---

## Python Example: 01_hello_world

### Challenge
Write a function that returns "Hello, World!"

### Solution
```python
def hello_world() -> str:
    """
    Return the string "Hello, World!"
    
    Returns:
        str: The string "Hello, World!"
    """
    return "Hello, World!"
```

### Why This Works
- Function is defined with the correct name
- Returns a string (not printing)
- Exact match including punctuation and capitalization

---

## C Example: 01_hello_world

### Challenge
Write a function that prints "Hello, World!"

### Solution
```c
#include <stdio.h>

/**
 * Print "Hello, World!" to the console
 */
void print_hello(void) {
    printf("Hello, World!\n");
}

int main() {
    print_hello();
    return 0;
}
```

### Why This Works
- Includes necessary header (stdio.h)
- Function prints exactly as required
- Includes newline character
- Main function calls the function

---

## Java Example: 01_hello_world

### Challenge
Write a method that returns "Hello, World!"

### Solution
```java
public class Solution {
    
    /**
     * Return the string "Hello, World!"
     * 
     * @return The string "Hello, World!"
     */
    public static String helloWorld() {
        return "Hello, World!";
    }
    
    public static void main(String[] args) {
        System.out.println(helloWorld());
    }
}
```

### Why This Works
- Method is public and static
- Returns String type
- Exact match of required string
- Main method for testing

---

## Testing Your Solutions

### Python
```bash
cd beginner/python/01_hello_world
pytest ../../tests/python/test_01_hello_world.py -v
```

Expected output:
```
test_01_hello_world.py::test_hello_world PASSED
test_01_hello_world.py::test_return_type PASSED
test_01_hello_world.py::test_exact_match PASSED

======================== 3 passed in 0.02s ========================
```

### C
```bash
cd beginner/c/01_hello_world
gcc solution.c -o solution
./solution
```

Expected output:
```
Hello, World!
```

### Java
```bash
cd beginner/java/01_hello_world
javac Solution.java
java Solution
```

Expected output:
```
Hello, World!
```

---

## Common Patterns

### Python Pattern: Simple Return
```python
def function_name(parameter):
    # Process parameter
    result = # ... computation
    return result
```

### C Pattern: Function with Parameters
```c
int function_name(int param1, int param2) {
    // Process parameters
    int result = // ... computation
    return result;
}
```

### Java Pattern: Static Method
```java
public static ReturnType methodName(ParamType param) {
    // Process parameter
    ReturnType result = // ... computation
    return result;
}
```

---

## Tips for Success

1. **Read the function signature carefully**
   - Match the exact name
   - Use correct parameter types
   - Return the correct type

2. **Pay attention to details**
   - Capitalization matters
   - Punctuation matters
   - Return vs. print

3. **Test incrementally**
   - Run tests after writing basic structure
   - Add functionality step by step
   - Verify each part works

4. **Use the examples in README**
   - Each challenge has example inputs/outputs
   - Use them to understand requirements
   - Test against all examples

---

## Next Steps

Now that you've seen examples:

1. Try solving 02_sum_two_numbers without looking at solutions
2. Use the pattern from the hello_world example
3. Read the README carefully for requirements
4. Run tests to verify your solution

**Remember:** The goal is learning, not just getting tests to pass. Understand *why* your solution works!

---

Good luck! 🚀
