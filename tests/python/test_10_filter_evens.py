"""
Test suite for Challenge 10: Filter Evens
"""
import sys
import os

challenge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../beginner/python/10_filter_evens'))
sys.path.insert(0, challenge_dir)

import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("solution_10", os.path.join(challenge_dir, "solution.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
filter_evens = solution_module.filter_evens


def test_mixed_numbers():
    """Test with mixed odd and even numbers"""
    result = filter_evens([1, 2, 3, 4, 5, 6])
    assert result == [2, 4, 6]


def test_only_odd():
    """Test with only odd numbers"""
    result = filter_evens([1, 3, 5, 7])
    assert result == []


def test_only_even():
    """Test with only even numbers"""
    result = filter_evens([2, 4, 6, 8])
    assert result == [2, 4, 6, 8]


def test_empty_list():
    """Test with empty list"""
    result = filter_evens([])
    assert result == []


def test_negative_numbers():
    """Test with negative numbers"""
    result = filter_evens([-2, -1, 0, 1, 2])
    assert result == [-2, 0, 2]


def test_zero():
    """Test that zero is included (zero is even)"""
    result = filter_evens([0])
    assert result == [0]


def test_order_preserved():
    """Test that original order is preserved"""
    result = filter_evens([10, 5, 8, 3, 2])
    assert result == [10, 8, 2]


def test_return_type():
    """Test that function returns a list"""
    result = filter_evens([1, 2, 3])
    assert isinstance(result, list)
