# Problem: Check if a number is an Armstrong number
# Approach: Count digits, then sum each digit raised to that power
# Example: 153 -> 1³ + 5³ + 3³ = 153
# Time Complexity: O(log10 n)
# Space Complexity: O(1)

class Solution:
    def armstrongNumber(self, n):

        # Negative numbers are not Armstrong numbers
        if n < 0:
            return False

        total = 0
        nod = len(str(n))
        num = n

        while n > 0:
            ld = n % 10
            total = total + ld ** nod
            n = n // 10

        return total == num


# Example test
obj = Solution()
print(obj.armstrongNumber(153))  # True
print(obj.armstrongNumber(123))  # False
