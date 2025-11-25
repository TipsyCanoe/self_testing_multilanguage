"""
Test suite for Challenge 05: Find Maximum
"""
import sys
import os

challenge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../beginner/python/05_find_max'))
sys.path.insert(0, challenge_dir)

import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("solution_05", os.path.join(challenge_dir, "solution.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
find_max = solution_module.find_max


def test_positive_numbers():
    """Test with positive numbers"""
    assert find_max([3, 7, 2, 9, 1]) == 9
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([100, 50, 75]) == 100


def test_negative_numbers():
    """Test with negative numbers"""
    assert find_max([-5, -2, -10, -1]) == -1
    assert find_max([-1, -2, -3]) == -1


def test_mixed_numbers():
    """Test with mixed positive and negative"""
    assert find_max([-5, 0, 5]) == 5
    assert find_max([10, -10, 20, -20]) == 20


def test_single_element():
    """Test with single element"""
    assert find_max([42]) == 42
    assert find_max([-5]) == -5


def test_duplicates():
    """Test with duplicate max values"""
    assert find_max([5, 5, 5, 5]) == 5
    assert find_max([1, 3, 3, 2]) == 3


def test_floats():
    """Test with floating point numbers"""
    assert find_max([5.5, 2.3, 8.1]) == pytest.approx(8.1)


def test_max_at_different_positions():
    """Test max at beginning, middle, and end"""
    assert find_max([9, 5, 3, 1]) == 9  # beginning
    assert find_max([1, 9, 5, 3]) == 9  # middle
    assert find_max([1, 3, 5, 9]) == 9  # end
