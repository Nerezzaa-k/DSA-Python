# Problem: Remove duplicates from a sorted array (in-place)
# Platform: LeetCode
# Approach: Two-pointer technique
# Example: [1,1,2,2,3] → [1,2,3,_ ,_] → return 3
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:

    def removeDuplicates(self, nums):

        n = len(nums)

        # Edge case
        if n == 1:
            return 1

        i = 0
        j = i + 1

        while j < n:

            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

            j += 1

        return i + 1


# Example test
obj = Solution()
arr = [1, 1, 2, 2, 3]
length = obj.removeDuplicates(arr)

print(length)       # Output: 3
print(arr[:length]) # Unique elements
