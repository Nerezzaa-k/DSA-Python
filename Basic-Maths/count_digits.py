# Problem: Count digits in a number
# Approach: Using logarithmic formula
# Formula: digits = floor(log10(n)) + 1
# Time Complexity: O(1)
# Space Complexity: O(1)

from math import log10

def countDigit(n):
    if n == 0:
        return 1
    return int(log10(abs(n))) + 1


# Example test
print(countDigit(12345))
