"""
Challenge 07: Reverse String
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text: A string to reverse
    
    Returns:
        str: The reversed string
    
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
        >>> reverse_string("")
        ''
    
    Multiple approaches:
        1. Slicing: text[::-1]
        2. reversed() + join: ''.join(reversed(text))
        3. Manual loop
    """
    # Method 1: Slicing (most pythonic)
    return text[::-1]
    
    # Method 2: Using reversed()
    # return ''.join(reversed(text))
    
    # Method 3: Manual (educational)
    # result = ""
    # for char in text:
    #     result = char + result
    # return result


if __name__ == "__main__":
    # Test cases
    test_cases = ["hello", "Python", "", "12345"]
    for test in test_cases:
        print(f"reverse_string('{test}') = '{reverse_string(test)}'")
