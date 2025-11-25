"""
Test suite for Challenge 02: Sum Two Numbers
"""
import sys
import os

# Add the specific challenge directory to path
challenge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../beginner/python/02_sum_two_numbers'))
sys.path.insert(0, challenge_dir)

import pytest
import importlib.util

# Import the solution module directly to avoid caching issues
spec = importlib.util.spec_from_file_location("solution_02", os.path.join(challenge_dir, "solution.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
sum_two = solution_module.sum_two


def test_positive_numbers():
    """Test with positive numbers"""
    assert sum_two(5, 3) == 8
    assert sum_two(10, 20) == 30
    assert sum_two(1, 1) == 2


def test_negative_numbers():
    """Test with negative numbers"""
    assert sum_two(-5, -3) == -8
    assert sum_two(-10, -20) == -30


def test_mixed_signs():
    """Test with mixed positive and negative"""
    assert sum_two(-2, 7) == 5
    assert sum_two(10, -5) == 5


def test_zero():
    """Test with zero"""
    assert sum_two(0, 0) == 0
    assert sum_two(5, 0) == 5
    assert sum_two(0, 10) == 10


def test_floats():
    """Test with floating point numbers"""
    assert sum_two(0.5, 0.3) == pytest.approx(0.8)
    assert sum_two(1.5, 2.5) == pytest.approx(4.0)
