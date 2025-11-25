"""
Challenge 04: List Sum
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def list_sum(numbers: list) -> float:
    """
    Calculate the sum of all numbers in a list.
    
    Args:
        numbers: A list of numbers
    
    Returns:
        float: The sum of all numbers
    
    Examples:
        >>> list_sum([1, 2, 3, 4, 5])
        15
        >>> list_sum([])
        0
        >>> list_sum([-1, -2, -3])
        -6
    
    Approach 1: Using built-in sum()
    Approach 2: Using a loop with accumulator
    """
    # Method 1: Using built-in (simple and pythonic)
    return sum(numbers)
    
    # Method 2: Manual loop (educational)
    # total = 0
    # for num in numbers:
    #     total += num
    # return total


if __name__ == "__main__":
    # Test cases
    print(f"list_sum([1, 2, 3, 4, 5]) = {list_sum([1, 2, 3, 4, 5])}")
    print(f"list_sum([]) = {list_sum([])}")
    print(f"list_sum([-1, -2, -3]) = {list_sum([-1, -2, -3])}")
