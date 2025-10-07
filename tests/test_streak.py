import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers returns 0."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a simple case with one streak."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3

def test_multiple_streaks_longest_last():
    """Test multiple streaks where the longest streak is at the end."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 4]) == 4

def test_multiple_streaks_longest_first():
    """Test multiple streaks where the longest streak is at the beginning."""
    assert longest_positive_streak([1, 2, 3, 4, 0, 1, 2]) == 4

def test_streaks_with_negatives():
    """Test that negative numbers break the streak."""
    assert longest_positive_streak([1, 2, -1, 4, 5, 6]) == 3

def test_streaks_with_zeros():
    """Test that zeros break the streak."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3

def test_streak_at_the_end():
    """Test a streak that goes to the end of the list."""
    assert longest_positive_streak([0, -1, 1, 2, 3]) == 3

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-1]) == 0

def test_complex_case():
    """Test a more complex case with multiple streaks of different lengths."""
    assert longest_positive_streak([1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, -5, 1]) == 4