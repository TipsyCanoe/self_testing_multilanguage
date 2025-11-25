"""
Challenge 02: Sum Two Numbers
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def sum_two(a: float, b: float) -> float:
    """
    Calculate the sum of two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        float: The sum of a and b
    
    Examples:
        >>> sum_two(5, 3)
        8
        >>> sum_two(-2, 7)
        5
        >>> sum_two(0.5, 0.3)
        0.8
    """
    return a + b


if __name__ == "__main__":
    # Test cases
    print(f"sum_two(5, 3) = {sum_two(5, 3)}")
    print(f"sum_two(-2, 7) = {sum_two(-2, 7)}")
    print(f"sum_two(0.5, 0.3) = {sum_two(0.5, 0.3)}")
