"""
Test suite for Challenge 08: Character Frequency
"""
import sys
import os

challenge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../beginner/python/08_char_frequency'))
sys.path.insert(0, challenge_dir)

import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("solution_08", os.path.join(challenge_dir, "solution.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
char_frequency = solution_module.char_frequency


def test_basic_string():
    """Test with basic string"""
    result = char_frequency("hello")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}


def test_repeated_characters():
    """Test with repeated characters"""
    result = char_frequency("aaa")
    assert result == {'a': 3}
    
    result = char_frequency("aabbcc")
    assert result == {'a': 2, 'b': 2, 'c': 2}


def test_empty_string():
    """Test with empty string"""
    result = char_frequency("")
    assert result == {}


def test_case_insensitive():
    """Test case insensitivity"""
    result = char_frequency("Hello")
    assert result == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    
    result = char_frequency("AaBbCc")
    assert result == {'a': 2, 'b': 2, 'c': 2}


def test_with_spaces():
    """Test with spaces"""
    result = char_frequency("a b c")
    assert result == {'a': 1, ' ': 2, 'b': 1, 'c': 1}


def test_with_numbers():
    """Test with numbers"""
    result = char_frequency("abc123")
    assert result['a'] == 1
    assert result['1'] == 1


def test_return_type():
    """Test that function returns a dictionary"""
    result = char_frequency("test")
    assert isinstance(result, dict)
