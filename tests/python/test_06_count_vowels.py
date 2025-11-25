"""
Test suite for Challenge 06: Count Vowels
"""
import sys
import os

challenge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../beginner/python/06_count_vowels'))
sys.path.insert(0, challenge_dir)

import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("solution_06", os.path.join(challenge_dir, "solution.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
count_vowels = solution_module.count_vowels


def test_lowercase_vowels():
    """Test with lowercase vowels"""
    assert count_vowels("hello") == 2
    assert count_vowels("aeiou") == 5


def test_uppercase_vowels():
    """Test with uppercase vowels"""
    assert count_vowels("HELLO") == 2
    assert count_vowels("AEIOU") == 5


def test_mixed_case():
    """Test with mixed case"""
    assert count_vowels("Programming") == 3
    assert count_vowels("Hello World") == 3


def test_no_vowels():
    """Test with no vowels"""
    assert count_vowels("xyz") == 0
    assert count_vowels("bcdfg") == 0


def test_empty_string():
    """Test with empty string"""
    assert count_vowels("") == 0


def test_only_vowels():
    """Test with only vowels"""
    assert count_vowels("aaa") == 3
    assert count_vowels("AEI") == 3


def test_with_spaces_and_punctuation():
    """Test with spaces and punctuation"""
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("a e i o u") == 5
