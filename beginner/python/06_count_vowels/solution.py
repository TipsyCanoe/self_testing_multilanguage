"""
Challenge 06: Count Vowels
TODO: Implement the count_vowels function
"""

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a string.
    
    Args:
        text: A string to analyze
    
    Returns:
        int: The number of vowels (a, e, i, o, u, A, E, I, O, U)
    """
    return count_vowels_helper(text) 

def count_vowels_helper(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    # Test your function
    print(f"count_vowels('hello') = {count_vowels('hello')}")
    print(f"count_vowels('AEIOU') = {count_vowels('AEIOU')}")
    print(f"count_vowels('xyz') = {count_vowels('xyz')}")
    print(f"count_vowels('Programming') = {count_vowels('Programming')}")
