"""
Unit tests for Fikra core functionality
"""

import pytest
from fikra import Fikra

def test_initialization():
    """Test that Fikra initializes without errors"""
    brain = Fikra()
    assert brain is not None

def test_basic_reasoning():
    """Test basic reasoning capability"""
    brain = Fikra()
    answer = brain.reason("What is 2 + 2?")
    assert answer is not None
    assert len(answer) > 0

def test_math_reasoning():
    """Test mathematical reasoning"""
    brain = Fikra()
    answer = brain.reason("If I have 5 apples and eat 2, how many are left?")
    assert "3" in answer

def test_max_tokens():
    """Test max_tokens parameter"""
    brain = Fikra()
    short = brain.reason("Explain AI", max_tokens=50)
    long = brain.reason("Explain AI", max_tokens=200)
    assert len(long) > len(short)

if __name__ == "__main__":
    pytest.main([__file__])
