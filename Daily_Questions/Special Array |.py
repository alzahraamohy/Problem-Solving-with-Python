# https://leetcode.com/problems/special-array-i/description/?envType=daily-question&envId=2025-02-01

class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:  # Check if adjacent elements have the same parity
                return False
        return True  # Return True only after checking all pairs
