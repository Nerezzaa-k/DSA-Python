# Problem: Linear Search in an array
# Approach: Traverse the array and compare each element with target
# Example: arr = [4, 2, 7, 1], x = 7 → Output: index = 2
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:

    def search(self, arr, x):

        for i in range(len(arr)):

            if arr[i] == x:
                return i

        return -1


# Example test
obj = Solution()
print(obj.search([4, 2, 7, 1], 7))  # Output: 2
print(obj.search([4, 2, 7, 1], 5))  # Output: -1
