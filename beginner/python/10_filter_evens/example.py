"""
Challenge 10: Filter Even Numbers
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def filter_evens(numbers: list) -> list:
    """
    Filter and return only the even numbers from a list.
    
    Args:
        numbers: A list of integers
    
    Returns:
        list: A list containing only the even numbers
    
    Examples:
        >>> filter_evens([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        >>> filter_evens([1, 3, 5, 7])
        []
        >>> filter_evens([])
        []
    
    Multiple approaches:
        1. List comprehension (most pythonic)
        2. filter() function
        3. Manual loop
    """
    # Method 1: List comprehension (recommended)
    return [num for num in numbers if num % 2 == 0]
    
    # Method 2: Using filter()
    # return list(filter(lambda x: x % 2 == 0, numbers))
    
    # Method 3: Manual loop (educational)
    # result = []
    # for num in numbers:
    #     if num % 2 == 0:
    #         result.append(num)
    # return result


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5, 6],
        [1, 3, 5, 7],
        [-2, -1, 0, 1, 2],
        []
    ]
    for test in test_cases:
        print(f"filter_evens({test}) = {filter_evens(test)}")
