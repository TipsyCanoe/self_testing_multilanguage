"""
Test suite for Challenge 07: Reverse String
"""
import sys
import os

challenge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../beginner/python/07_reverse_string'))
sys.path.insert(0, challenge_dir)

import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("solution_07", os.path.join(challenge_dir, "solution.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
reverse_string = solution_module.reverse_string


def test_normal_string():
    """Test with normal strings"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"


def test_single_character():
    """Test with single character"""
    assert reverse_string("a") == "a"
    assert reverse_string("Z") == "Z"


def test_empty_string():
    """Test with empty string"""
    assert reverse_string("") == ""


def test_numbers():
    """Test with numeric strings"""
    assert reverse_string("12345") == "54321"
    assert reverse_string("100") == "001"


def test_palindrome():
    """Test with palindromes"""
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("noon") == "noon"


def test_with_spaces():
    """Test with spaces"""
    assert reverse_string("hello world") == "dlrow olleh"
    assert reverse_string("a b c") == "c b a"


def test_with_punctuation():
    """Test with punctuation"""
    assert reverse_string("Hello!") == "!olleH"
