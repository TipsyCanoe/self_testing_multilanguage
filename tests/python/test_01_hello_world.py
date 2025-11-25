"""
Test suite for Challenge 01: Hello World
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../beginner/python/01_hello_world'))

import pytest
from solution import hello_world


def test_hello_world():
    """Test that the function returns 'Hello, World!'"""
    assert hello_world() == "Hello, World!"


def test_return_type():
    """Test that the function returns a string"""
    result = hello_world()
    assert isinstance(result, str)


def test_exact_match():
    """Test exact string match including punctuation"""
    result = hello_world()
    assert result == "Hello, World!"
    assert not result == "hello, world!"
    assert not result == "Hello World"
