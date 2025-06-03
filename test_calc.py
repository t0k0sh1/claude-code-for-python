import pytest
from calc import add


class TestAdd:
    """Test suite for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
        assert add(100, 200) == 300

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, -20) == -30
        assert add(-100, -200) == -300

    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(10, -5) == 5
        assert add(-10, 5) == -5
        assert add(100, -100) == 0

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)
        assert add(-1.5, 2.5) == 1.0

    def test_add_with_zero(self):
        """Test adding with zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(-5, 0) == -5

    def test_add_none_raises_value_error(self):
        """Test that None arguments raise ValueError."""
        with pytest.raises(ValueError, match="Arguments cannot be None"):
            add(None, 5)
        
        with pytest.raises(ValueError, match="Arguments cannot be None"):
            add(5, None)
        
        with pytest.raises(ValueError, match="Arguments cannot be None"):
            add(None, None)

    def test_add_non_numeric_raises_value_error(self):
        """Test that non-numeric arguments raise ValueError."""
        with pytest.raises(ValueError, match="Arguments must be numeric"):
            add("5", 3)
        
        with pytest.raises(ValueError, match="Arguments must be numeric"):
            add(5, "3")
        
        with pytest.raises(ValueError, match="Arguments must be numeric"):
            add([1, 2], 3)
        
        with pytest.raises(ValueError, match="Arguments must be numeric"):
            add(5, {"a": 1})
        
        with pytest.raises(ValueError, match="Arguments must be numeric"):
            add(True, 5)  # bool is not included in our numeric types