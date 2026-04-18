# Problem: Check whether a number is prime
# Approach: Check divisibility from 2 to sqrt(n)
# Example: 7 → Prime (only divisible by 1 and itself)
# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

import math


class Solution:

    def isPrime(self, n):

        # Numbers <= 1 are not prime
        if n <= 1:
            return False

        # Check divisibility up to sqrt(n)
        for i in range(2, int(math.sqrt(n)) + 1):

            if n % i == 0:
                return False

        return True


# Example test
obj = Solution()
print(obj.isPrime(7))   # True
print(obj.isPrime(12))  # False
