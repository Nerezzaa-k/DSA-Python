# Problem: Check if an array is sorted in non-decreasing order
# Approach: Compare each element with the next element
# Example: [1, 2, 2, 4, 5] → True
# Example: [1, 3, 2, 5] → False
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:

    def isSorted(self, arr) -> bool:

        n = len(arr)

        for i in range(n - 1):

            if arr[i] > arr[i + 1]:
                return False

        return True


# Example test
obj = Solution()
print(obj.isSorted([1, 2, 3, 4, 5]))  # True
print(obj.isSorted([1, 3, 2, 4]))     # False
