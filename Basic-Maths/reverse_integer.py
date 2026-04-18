# Problem: Reverse Integer
# Platform: LeetCode
# Approach: Extract digits using modulus and rebuild reversed number
# Handles negative numbers and overflow (32-bit integer constraint)
# Time Complexity: O(log10 n)
# Space Complexity: O(1)

class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1

        x = abs(x)
        result = 0

        while x > 0:
            ld = x % 10
            result = (result * 10) + ld
            x = x // 10

        result = sign * result

        # Handle 32-bit overflow condition
        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result


# Example test
obj = Solution()
print(obj.reverse(123))
print(obj.reverse(-456))
