"""
Challenge 08: Character Frequency
TODO: Implement the char_frequency function
"""

def char_frequency(text: str) -> dict:
    """
    Count the frequency of each character in a string (case-insensitive).
    
    Args:
        text: A string to analyze
    
    Returns:
        dict: A dictionary with characters as keys and frequencies as values
    """
    return char_frequency_helper(text)

def char_frequency_helper(text):
    char_frequency = {} 
    for char in text.lower():
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

if __name__ == "__main__":
    # Test your function
    print(f"char_frequency('hello') = {char_frequency('hello')}")
    print(f"char_frequency('aaa') = {char_frequency('aaa')}")
    print(f"char_frequency('Hello') = {char_frequency('Hello')}")
