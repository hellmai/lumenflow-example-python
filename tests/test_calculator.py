"""Tests for the calculator module."""

import pytest

from src.calculator import add, divide, multiply, subtract


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self) -> None:
        """Test adding two positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self) -> None:
        """Test adding two negative numbers."""
        assert add(-1, -2) == -3

    def test_add_zero(self) -> None:
        """Test adding zero."""
        assert add(5, 0) == 5


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self) -> None:
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2

    def test_subtract_negative_result(self) -> None:
        """Test subtraction with negative result."""
        assert subtract(3, 5) == -2


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self) -> None:
        """Test multiplying two positive numbers."""
        assert multiply(4, 3) == 12

    def test_multiply_by_zero(self) -> None:
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive_numbers(self) -> None:
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5

    def test_divide_by_zero_raises_error(self) -> None:
        """Test that dividing by zero raises an error."""
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            divide(10, 0)

    def test_divide_decimal_result(self) -> None:
        """Test division with decimal result."""
        assert divide(5, 2) == 2.5
