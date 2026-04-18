# Problem: Find the largest element in an array
# Approach: Traverse the array and keep updating the maximum value
# Example: [3, 7, 2, 9, 5] → Output: 9
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:

    def largest(self, arr):

        # Assume first element is largest initially
        largest = arr[0]

        # Traverse array
        for i in range(len(arr)):
            largest = max(largest, arr[i])

        return largest


# Example test
obj = Solution()
print(obj.largest([3, 7, 2, 9, 5]))  # Output: 9
