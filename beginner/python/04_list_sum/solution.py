"""
Challenge 04: List Sum
TODO: Implement the list_sum function
"""

def list_sum(numbers: list) -> float:
    """
    Calculate the sum of all numbers in a list.
    
    Args:
        numbers: A list of numbers
    
    Returns:
        float: The sum of all numbers
    """
    return sum_list(numbers)

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


if __name__ == "__main__":
    # Test your function
    print(f"list_sum([1, 2, 3, 4, 5]) = {list_sum([1, 2, 3, 4, 5])}")
    print(f"list_sum([-1, -2, -3]) = {list_sum([-1, -2, -3])}")
    print(f"list_sum([]) = {list_sum([])}")
