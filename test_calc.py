import pytest
from calc import add


class TestAdd:
    """Test suite for the add function."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 3, 5),
            (10, 20, 30),
            (100, 200, 300),
        ],
    )
    def test_add_positive_numbers(self, a, b, expected):
        """Test adding two positive numbers."""
        assert add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (-2, -3, -5),
            (-10, -20, -30),
            (-100, -200, -300),
        ],
    )
    def test_add_negative_numbers(self, a, b, expected):
        """Test adding negative numbers."""
        assert add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (10, -5, 5),
            (-10, 5, -5),
            (100, -100, 0),
        ],
    )
    def test_add_mixed_numbers(self, a, b, expected):
        """Test adding positive and negative numbers."""
        assert add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1.5, 2.5, 4.0),
            (0.1, 0.2, pytest.approx(0.3)),
            (-1.5, 2.5, 1.0),
        ],
    )
    def test_add_floats(self, a, b, expected):
        """Test adding floating point numbers."""
        assert add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (0, 0, 0),
            (5, 0, 5),
            (0, 5, 5),
            (-5, 0, -5),
        ],
    )
    def test_add_with_zero(self, a, b, expected):
        """Test adding with zero."""
        assert add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b",
        [
            (None, 5),
            (5, None),
            (None, None),
        ],
    )
    def test_add_none_raises_value_error(self, a, b):
        """Test that None arguments raise ValueError."""
        with pytest.raises(ValueError, match="Arguments cannot be None"):
            add(a, b)

    @pytest.mark.parametrize(
        "a, b",
        [
            ("5", 3),
            (5, "3"),
            ([1, 2], 3),
            (5, {"a": 1}),
            (True, 5),  # bool is not included in our numeric types
        ],
    )
    def test_add_non_numeric_raises_value_error(self, a, b):
        """Test that non-numeric arguments raise ValueError."""
        with pytest.raises(ValueError, match="Arguments must be numeric"):
            add(a, b)
