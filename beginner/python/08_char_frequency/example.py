"""
Challenge 08: Character Frequency
This file contains a working example solution.
Study it, then implement your own in solution.py
"""

def char_frequency(text: str) -> dict:
    """
    Count the frequency of each character in a string (case-insensitive).
    
    Args:
        text: A string to analyze
    
    Returns:
        dict: A dictionary with characters as keys and frequencies as values
    
    Examples:
        >>> char_frequency("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        >>> char_frequency("aaa")
        {'a': 3}
        >>> char_frequency("")
        {}
    
    Approach:
        1. Convert to lowercase
        2. Use dictionary to count occurrences
        3. Can also use collections.Counter
    """
    # Method 1: Manual dictionary
    freq = {}
    for char in text.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
    
    # Method 2: Using get() method (cleaner)
    # freq = {}
    # for char in text.lower():
    #     freq[char] = freq.get(char, 0) + 1
    # return freq
    
    # Method 3: Using Counter (advanced)
    # from collections import Counter
    # return dict(Counter(text.lower()))


if __name__ == "__main__":
    # Test cases
    test_cases = ["hello", "aaa", "Hello"]
    for test in test_cases:
        print(f"char_frequency('{test}') = {char_frequency(test)}")
