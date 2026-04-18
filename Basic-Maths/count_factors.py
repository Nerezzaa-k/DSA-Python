# Problem: Count number of factors of a number
# Approach: Iterate till sqrt(n) and count divisor pairs
# Example: 12 → factors = 1, 2, 3, 4, 6, 12 → total = 6
# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

import math


class Solution:

    def countFactors(self, n):

        # Edge case
        if n <= 0:
            return 0

        count = 0

        for i in range(1, int(math.sqrt(n)) + 1):

            if n % i == 0:

                # Perfect square case
                if i == n // i:
                    count += 1

                else:
                    count += 2

        return count


# Example test
obj = Solution()
print(obj.countFactors(12))  # Output: 6
