"""
Challenge 09: FizzBuzz
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def fizzbuzz(n: int) -> list:
    """
    Generate FizzBuzz sequence from 1 to n.
    
    Args:
        n: The upper limit (inclusive)
    
    Returns:
        list: FizzBuzz sequence with numbers and strings
    
    Examples:
        >>> fizzbuzz(5)
        [1, 2, 'Fizz', 4, 'Buzz']
        >>> fizzbuzz(15)[-1]
        'FizzBuzz'
    
    Rules:
        - Divisible by 3 and 5: "FizzBuzz"
        - Divisible by 3: "Fizz"
        - Divisible by 5: "Buzz"
        - Otherwise: the number itself
    
    Important: Check divisible by 15 FIRST!
    """
    result = []
    
    for i in range(1, n + 1):
        # Check 15 first (both 3 and 5)
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    
    return result


if __name__ == "__main__":
    # Test cases
    print(f"fizzbuzz(5) = {fizzbuzz(5)}")
    print(f"fizzbuzz(15) = {fizzbuzz(15)}")
