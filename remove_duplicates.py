# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j