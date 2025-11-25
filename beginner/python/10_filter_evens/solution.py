"""
Challenge 10: Filter Even Numbers
TODO: Implement the filter_evens function
"""

def filter_evens(numbers: list) -> list:
    """
    Filter and return only the even numbers from a list.
    
    Args:
        numbers: A list of integers
    
    Returns:
        list: A list containing only the even numbers
    """
    return filter_evens_helper(numbers)

def filter_evens_helper(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers    
        


if __name__ == "__main__":
    # Test your function
    print(f"filter_evens([1, 2, 3, 4, 5, 6]) = {filter_evens([1, 2, 3, 4, 5, 6])}")
    print(f"filter_evens([1, 3, 5, 7]) = {filter_evens([1, 3, 5, 7])}")
    print(f"filter_evens([-2, -1, 0, 1, 2]) = {filter_evens([-2, -1, 0, 1, 2])}")
