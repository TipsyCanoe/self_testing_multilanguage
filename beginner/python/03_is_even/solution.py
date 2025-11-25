"""
Challenge 03: Is Even
TODO: Implement the is_even function
"""

def is_even(n: int) -> bool:
    """
    Determine if a number is even.
    
    Args:
        n: An integer to check
    
    Returns:
        bool: True if n is even, False otherwise
    """
    return n % 2 == 0


if __name__ == "__main__":
    # Test your function
    print(f"is_even(4) = {is_even(4)}")
    print(f"is_even(7) = {is_even(7)}")
    print(f"is_even(0) = {is_even(0)}")
    print(f"is_even(-2) = {is_even(-2)}")
