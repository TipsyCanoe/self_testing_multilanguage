"""
Challenge 07: Reverse String
TODO: Implement the reverse_string function
"""

def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text: A string to reverse
    
    Returns:
        str: The reversed string
    """
    return reverse_string_helper(text)

def reverse_string_helper(text): 
    if text == "":
        return text
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text
        
        
        
if __name__ == "__main__":
    # Test your function
    print(f"reverse_string('hello') = {reverse_string('hello')}")
    print(f"reverse_string('Python') = {reverse_string('Python')}")
    print(f"reverse_string('') = '{reverse_string('')}'")
