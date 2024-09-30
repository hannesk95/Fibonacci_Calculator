"""Provides code to calcualte fibonacci numbers."""

from typing import List

import fire


def fibonacci_sequence(start: int, length: int) -> List[int]:
    """Generate Fibonacci sequence.

    Args:
        start (int): The number from which to start generating the Fibonacci sequence.
        length (int): The number of Fibonacci numbers to return.

    Returns:
        List[int]: A list of Fibonacci numbers.
    """

    def next_fibonacci(a: int, b: int) -> int:
        """Given two numbers, this function returns the next fibonacci item.

        Args:
            a (int): First number
            b (int): Second number

        Returns:
            int: Next fibonacci item
        """
        return a + b

    # Start the Fibonacci sequence with the first two numbers
    fib_1, fib_2 = 0, 1
    result = []

    # Find the first Fibonacci number >= start
    while fib_2 < start:
        fib_1, fib_2 = fib_2, next_fibonacci(fib_1, fib_2)

    # Append Fibonacci numbers to the result starting from the found number
    for _ in range(length):
        result.append(fib_2)
        fib_1, fib_2 = fib_2, next_fibonacci(fib_1, fib_2)

    return result


if __name__ == '__main__':

    # Example usage
    # start_number = 13
    # subsequent_fibonacci = fire.Fire(fibonacci_sequence(start_number, 5))
    subsequent_fibonacci = fire.Fire(fibonacci_sequence)
    # print(subsequent_fibonacci)  # Output: [13, 21, 34, 55, 89]
