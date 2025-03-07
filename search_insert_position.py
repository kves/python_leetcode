# https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(nums, target):
        first = 0
        last = len(nums) - 1

        while first <= last:
            middle = int(first + last / 2)
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                first = middle + 1
            else:
                last = middle - 1
        if nums[middle] < target:
            return middle + 1
        return middle


list = [1, 3, 5, 6]
print(Solution.searchInsert(list, 2))
