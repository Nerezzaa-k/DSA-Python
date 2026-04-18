# Problem: Move all zeroes to the end of the array
# Platform: LeetCode
# Approach: Two-pointer technique (swap non-zero elements forward)
# Example: [0,1,0,3,12] → [1,3,12,0,0]
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:

    def moveZeroes(self, nums):

        # Edge case
        if len(nums) == 1:
            return

        i = 0

        # Find first zero position
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1

        # If no zero found
        if i == len(nums):
            return

        j = i + 1

        # Move non-zero elements forward
        while j < len(nums):

            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

            j += 1


# Example test
arr = [0, 1, 0, 3, 12]
Solution().moveZeroes(arr)
print(arr)   # Output: [1, 3, 12, 0, 0]
