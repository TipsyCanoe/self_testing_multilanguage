"""
Test suite for Challenge 09: FizzBuzz
"""
import sys
import os

challenge_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../beginner/python/09_fizzbuzz'))
sys.path.insert(0, challenge_dir)

import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("solution_09", os.path.join(challenge_dir, "solution.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
fizzbuzz = solution_module.fizzbuzz


def test_fizzbuzz_5():
    """Test FizzBuzz for n=5"""
    result = fizzbuzz(5)
    assert result == [1, 2, "Fizz", 4, "Buzz"]


def test_fizzbuzz_15():
    """Test FizzBuzz for n=15"""
    result = fizzbuzz(15)
    expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 
                11, "Fizz", 13, 14, "FizzBuzz"]
    assert result == expected


def test_fizzbuzz_1():
    """Test FizzBuzz for n=1"""
    result = fizzbuzz(1)
    assert result == [1]


def test_divisible_by_3():
    """Test numbers divisible by 3"""
    result = fizzbuzz(9)
    assert result[2] == "Fizz"  # 3
    assert result[5] == "Fizz"  # 6
    assert result[8] == "Fizz"  # 9


def test_divisible_by_5():
    """Test numbers divisible by 5"""
    result = fizzbuzz(10)
    assert result[4] == "Buzz"  # 5
    assert result[9] == "Buzz"  # 10


def test_divisible_by_15():
    """Test numbers divisible by both 3 and 5"""
    result = fizzbuzz(30)
    assert result[14] == "FizzBuzz"  # 15
    assert result[29] == "FizzBuzz"  # 30


def test_return_type():
    """Test that function returns a list"""
    result = fizzbuzz(5)
    assert isinstance(result, list)


def test_length():
    """Test that result length matches n"""
    assert len(fizzbuzz(10)) == 10
    assert len(fizzbuzz(20)) == 20
