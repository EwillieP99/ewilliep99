## Hi there 👋

# Fibonacci Sequence Implementation

This repository contains a comprehensive implementation of the Fibonacci sequence in Python, demonstrating multiple approaches and best practices.

## Features

- **Multiple Implementations**: Iterative and recursive approaches
- **Sequence Generator**: Generate multiple Fibonacci numbers at once
- **Well-Documented**: Complete docstrings and examples
- **Fully Tested**: Comprehensive unit tests with edge cases
- **Error Handling**: Proper validation and error messages

## Usage

### Running the Demo

```bash
python3 fibonacci.py
```

### Using in Your Code

```python
from fibonacci import fibonacci_iterative, fibonacci_sequence

# Calculate the 10th Fibonacci number
result = fibonacci_iterative(10)
print(f"F(10) = {result}")  # Output: F(10) = 55

# Generate the first 10 Fibonacci numbers
sequence = fibonacci_sequence(10)
print(sequence)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Testing

Run the unit tests to verify the implementation:

```bash
python3 test_fibonacci.py
```

Or use unittest discovery:

```bash
python3 -m unittest discover
```

## Fibonacci Sequence

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones:

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
```

Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

<!--
**EwillieP99/ewilliep99** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.
-->
