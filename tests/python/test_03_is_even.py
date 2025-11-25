"""
Test suite for Challenge 03: Is Even
"""
import sys
import os

challenge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../beginner/python/03_is_even'))
sys.path.insert(0, challenge_dir)

import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("solution_03", os.path.join(challenge_dir, "solution.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
is_even = solution_module.is_even


def test_positive_even():
    """Test with positive even numbers"""
    assert is_even(2) is True
    assert is_even(4) is True
    assert is_even(100) is True


def test_positive_odd():
    """Test with positive odd numbers"""
    assert is_even(1) is False
    assert is_even(7) is False
    assert is_even(99) is False


def test_negative_even():
    """Test with negative even numbers"""
    assert is_even(-2) is True
    assert is_even(-4) is True


def test_negative_odd():
    """Test with negative odd numbers"""
    assert is_even(-1) is False
    assert is_even(-3) is False


def test_zero():
    """Test with zero (should be even)"""
    assert is_even(0) is True


def test_return_type():
    """Test that function returns boolean"""
    result = is_even(4)
    assert isinstance(result, bool)
