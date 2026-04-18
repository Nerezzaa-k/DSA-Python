# Problem: Rotate array to the right by k steps
# Platform: LeetCode
# Approach: Reverse array in three steps
# Example: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:

    def rotate(self, nums, k):

        n = len(nums)

        # Handle cases where k > n
        k = k % n

        # Helper function to reverse array section
        def reverse(nums, left, right):

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Reverse last k elements
        reverse(nums, n - k, n - 1)

        # Reverse first n-k elements
        reverse(nums, 0, n - k - 1)

        # Reverse whole array
        reverse(nums, 0, n - 1)


# Example test
arr = [1,2,3,4,5,6,7]
Solution().rotate(arr, 3)
print(arr)   # Output: [5,6,7,1,2,3,4]
