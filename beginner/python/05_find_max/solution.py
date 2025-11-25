"""
Challenge 05: Find Maximum
TODO: Implement the find_max function without using max()
"""

def find_max(numbers: list) -> float:
    """
    Find the maximum value in a list (without using max()).
    
    Args:
        numbers: A list of numbers (at least one element)
    
    Returns:
        float: The maximum value in the list
    """
    return find_max_helper(numbers)

def find_max_helper(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


if __name__ == "__main__":
    # Test your function
    print(f"find_max([3, 7, 2, 9, 1]) = {find_max([3, 7, 2, 9, 1])}")
    print(f"find_max([-5, -2, -10, -1]) = {find_max([-5, -2, -10, -1])}")
    print(f"find_max([42]) = {find_max([42])}")
