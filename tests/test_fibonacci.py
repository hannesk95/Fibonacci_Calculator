import unittest
from typing import List
from src.calculator import fibonacci_sequence 

class TestFibonacciSequence(unittest.TestCase):
    
    def test_fibonacci_sequence_start_in_sequence(self):
        # Test when the start number is already a Fibonacci number
        self.assertEqual(fibonacci_sequence(13, 5), [13, 21, 34, 55, 89])
    
    def test_fibonacci_sequence_start_not_in_sequence(self):
        # Test when the start number is not a Fibonacci number
        self.assertEqual(fibonacci_sequence(15, 5), [21, 34, 55, 89, 144])
    
    def test_fibonacci_sequence_start_with_small_value(self):
        # Test when the start number is smaller than any Fibonacci number (starting from 0)
        self.assertEqual(fibonacci_sequence(0, 6), [1, 1, 2, 3, 5, 8])
    
    def test_fibonacci_sequence_single_length(self):
        # Test when length of the sequence is 1
        self.assertEqual(fibonacci_sequence(34, 1), [34])
    
    def test_fibonacci_sequence_large_start(self):
        # Test when the start number is very large (e.g., greater than any small Fibonacci number)
        self.assertEqual(fibonacci_sequence(1000, 3), [1597, 2584, 4181])

    def test_fibonacci_sequence_start_with_negative(self):
        # Test when the start number is negative, the Fibonacci sequence should start from 1
        self.assertEqual(fibonacci_sequence(-5, 5), [1, 1, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()
