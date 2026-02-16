#!/usr/bin/env python3
"""
Unit tests for Fibonacci implementations.
"""

import unittest
from fibonacci import fibonacci_iterative, fibonacci_recursive, fibonacci_sequence


class TestFibonacciIterative(unittest.TestCase):
    """Test cases for the iterative Fibonacci implementation."""
    
    def test_base_cases(self):
        """Test base cases: F(0) = 0 and F(1) = 1."""
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)
    
    def test_small_numbers(self):
        """Test small Fibonacci numbers."""
        self.assertEqual(fibonacci_iterative(2), 1)
        self.assertEqual(fibonacci_iterative(3), 2)
        self.assertEqual(fibonacci_iterative(4), 3)
        self.assertEqual(fibonacci_iterative(5), 5)
        self.assertEqual(fibonacci_iterative(6), 8)
    
    def test_medium_numbers(self):
        """Test medium Fibonacci numbers."""
        self.assertEqual(fibonacci_iterative(10), 55)
        self.assertEqual(fibonacci_iterative(15), 610)
        self.assertEqual(fibonacci_iterative(20), 6765)
    
    def test_negative_input(self):
        """Test that negative input raises ValueError."""
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)
        with self.assertRaises(ValueError):
            fibonacci_iterative(-10)


class TestFibonacciRecursive(unittest.TestCase):
    """Test cases for the recursive Fibonacci implementation."""
    
    def test_base_cases(self):
        """Test base cases: F(0) = 0 and F(1) = 1."""
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
    
    def test_small_numbers(self):
        """Test small Fibonacci numbers."""
        self.assertEqual(fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci_recursive(4), 3)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_recursive(6), 8)
    
    def test_medium_numbers(self):
        """Test medium Fibonacci numbers (avoiding large n due to performance)."""
        self.assertEqual(fibonacci_recursive(10), 55)
    
    def test_negative_input(self):
        """Test that negative input raises ValueError."""
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)
        with self.assertRaises(ValueError):
            fibonacci_recursive(-10)


class TestFibonacciSequence(unittest.TestCase):
    """Test cases for the Fibonacci sequence generator."""
    
    def test_empty_sequence(self):
        """Test generating 0 Fibonacci numbers."""
        self.assertEqual(fibonacci_sequence(0), [])
    
    def test_single_number(self):
        """Test generating 1 Fibonacci number."""
        self.assertEqual(fibonacci_sequence(1), [0])
    
    def test_two_numbers(self):
        """Test generating 2 Fibonacci numbers."""
        self.assertEqual(fibonacci_sequence(2), [0, 1])
    
    def test_small_sequence(self):
        """Test generating a small sequence."""
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])
    
    def test_medium_sequence(self):
        """Test generating a medium sequence."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci_sequence(10), expected)
    
    def test_negative_input(self):
        """Test that negative input raises ValueError."""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-5)


class TestConsistency(unittest.TestCase):
    """Test that different implementations produce consistent results."""
    
    def test_iterative_vs_recursive(self):
        """Test that iterative and recursive methods produce the same results."""
        for i in range(15):  # Limited range for recursive performance
            with self.subTest(i=i):
                self.assertEqual(
                    fibonacci_iterative(i),
                    fibonacci_recursive(i),
                    f"Mismatch at position {i}"
                )
    
    def test_sequence_matches_iterative(self):
        """Test that sequence generator matches iterative implementation."""
        sequence = fibonacci_sequence(20)
        for i, value in enumerate(sequence):
            with self.subTest(i=i):
                self.assertEqual(
                    value,
                    fibonacci_iterative(i),
                    f"Mismatch at position {i}"
                )


if __name__ == "__main__":
    unittest.main()
