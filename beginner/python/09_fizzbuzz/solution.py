"""
Challenge 09: FizzBuzz
TODO: Implement the fizzbuzz function
"""

def fizzbuzz(n: int) -> list:
    """
    Generate FizzBuzz sequence from 1 to n.
    
    Args:
        n: The upper limit (inclusive)
    
    Returns:
        list: FizzBuzz sequence with numbers and strings
    """
    return fizzbuzz_helper(n)

def fizzbuzz_helper(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

if __name__ == "__main__":
    # Test your function
    print(f"fizzbuzz(5) = {fizzbuzz(5)}")
    print(f"fizzbuzz(15) = {fizzbuzz(15)}")
