"""
Challenge 03: Is Even
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def is_even(n: int) -> bool:
    """
    Determine if a number is even.
    
    Args:
        n: An integer to check
    
    Returns:
        bool: True if n is even, False otherwise
    
    Examples:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
        >>> is_even(0)
        True
    
    Tip: A number is even if it's divisible by 2 (remainder is 0)
    """
    return n % 2 == 0


if __name__ == "__main__":
    # Test cases
    test_cases = [4, 7, 0, -2, -3]
    for num in test_cases:
        print(f"is_even({num}) = {is_even(num)}")
