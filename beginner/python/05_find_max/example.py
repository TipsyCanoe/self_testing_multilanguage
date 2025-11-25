"""
Challenge 05: Find Maximum
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def find_max(numbers: list) -> float:
    """
    Find the maximum value in a list (without using max()).
    
    Args:
        numbers: A list of numbers (at least one element)
    
    Returns:
        float: The maximum value in the list
    
    Examples:
        >>> find_max([3, 7, 2, 9, 1])
        9
        >>> find_max([-5, -2, -10, -1])
        -1
        >>> find_max([42])
        42
    
    Algorithm:
        1. Start with first element as max
        2. Compare each element with current max
        3. Update max if element is larger
    """
    # Start with first element
    max_val = numbers[0]
    
    # Check each remaining element
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    
    return max_val


if __name__ == "__main__":
    # Test cases
    print(f"find_max([3, 7, 2, 9, 1]) = {find_max([3, 7, 2, 9, 1])}")
    print(f"find_max([-5, -2, -10, -1]) = {find_max([-5, -2, -10, -1])}")
    print(f"find_max([42]) = {find_max([42])}")
