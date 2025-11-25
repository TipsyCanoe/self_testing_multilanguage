"""
Challenge 01: Hello World
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def hello_world() -> str:
    """
    Return the string "Hello, World!"
    
    Returns:
        str: The string "Hello, World!"
    
    Example:
        >>> hello_world()
        'Hello, World!'
    """
    return "Hello, World!"


if __name__ == "__main__":
    # Test the function
    result = hello_world()
    print(result)
    print(f"Type: {type(result)}")
    print(f"Length: {len(result)}")
