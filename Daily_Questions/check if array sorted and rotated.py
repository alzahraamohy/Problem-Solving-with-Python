# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2025-02-02
class Solution(object):
    def check(self, nums):
        count_breaks = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                count_breaks += 1
            if count_breaks > 1:
                return False
        return True
                

        
