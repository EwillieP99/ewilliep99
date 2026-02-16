#!/usr/bin/env python3
"""
Fibonacci Sequence Implementation

This module provides multiple ways to calculate Fibonacci numbers.
"""

from functools import lru_cache


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> fibonacci_iterative(0)
        0
        >>> fibonacci_iterative(1)
        1
        >>> fibonacci_iterative(10)
        55
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


@lru_cache(maxsize=None)
def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using a recursive approach with memoization.
    
    This implementation uses @lru_cache decorator to memoize results, improving
    performance from O(2^n) to O(n) time complexity.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> fibonacci_recursive(0)
        0
        >>> fibonacci_recursive(1)
        1
        >>> fibonacci_recursive(10)
        55
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_sequence(n):
    """
    Generate the first n Fibonacci numbers.
    
    Args:
        n (int): The number of Fibonacci numbers to generate
        
    Returns:
        list: A list containing the first n Fibonacci numbers
        
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    
    return sequence


def main():
    """
    Main function to demonstrate Fibonacci calculations.
    """
    print("Fibonacci Sequence Demonstration")
    print("=" * 40)
    
    # Show first 15 Fibonacci numbers
    print("\nFirst 15 Fibonacci numbers:")
    sequence = fibonacci_sequence(15)
    print(sequence)
    
    # Show specific Fibonacci numbers
    print("\nSpecific Fibonacci numbers:")
    for i in [0, 1, 5, 10, 15, 20]:
        print(f"F({i}) = {fibonacci_iterative(i)}")


if __name__ == "__main__":
    main()
