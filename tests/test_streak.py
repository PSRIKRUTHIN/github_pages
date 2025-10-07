import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_streak():
    """Test a simple case with a single streak."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks():
    """Test with multiple streaks to ensure the longest is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_streaks_with_zero():
    """Test that zero correctly breaks a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_streaks_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, -2, 3, 4]) == 2

def test_all_non_positive():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -10]) == 0

def test_long_list():
    """Test with a longer list and multiple streaks."""
    assert longest_positive_streak([1, 2, 3, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1]) == 4

def test_identical_values():
    """Test with a streak of identical positive values."""
    assert longest_positive_streak([1, 1, 1]) == 3