"""
Test suite for Challenge 04: List Sum
"""
import sys
import os

challenge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../beginner/python/04_list_sum'))
sys.path.insert(0, challenge_dir)

import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("solution_04", os.path.join(challenge_dir, "solution.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
list_sum = solution_module.list_sum


def test_positive_numbers():
    """Test with positive numbers"""
    assert list_sum([1, 2, 3, 4, 5]) == 15
    assert list_sum([10, 20, 30]) == 60


def test_negative_numbers():
    """Test with negative numbers"""
    assert list_sum([-1, -2, -3]) == -6
    assert list_sum([-10, -20]) == -30


def test_mixed_numbers():
    """Test with mixed positive and negative"""
    assert list_sum([1, -1, 2, -2]) == 0
    assert list_sum([10, -5, 3]) == 8


def test_single_element():
    """Test with single element"""
    assert list_sum([10]) == 10
    assert list_sum([-5]) == -5


def test_empty_list():
    """Test with empty list"""
    assert list_sum([]) == 0


def test_floats():
    """Test with floating point numbers"""
    assert list_sum([1.5, 2.5, 3.0]) == pytest.approx(7.0)


def test_zeros():
    """Test with zeros"""
    assert list_sum([0, 0, 0]) == 0
