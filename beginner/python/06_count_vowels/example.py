"""
Challenge 06: Count Vowels
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a string.
    
    Args:
        text: A string to analyze
    
    Returns:
        int: The number of vowels (a, e, i, o, u, A, E, I, O, U)
    
    Examples:
        >>> count_vowels("hello")
        2
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("xyz")
        0
    
    Approach 1: Check each character against vowel string
    Approach 2: Use set for faster lookup
    """
    # Method 1: Simple and clear
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
    
    # Method 2: More pythonic using sum
    # return sum(1 for char in text if char.lower() in 'aeiou')


if __name__ == "__main__":
    # Test cases
    test_cases = ["hello", "AEIOU", "xyz", "Programming"]
    for test in test_cases:
        print(f"count_vowels('{test}') = {count_vowels(test)}")
