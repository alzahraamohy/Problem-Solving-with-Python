# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2025-02-03
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc = 1
        dec = 1
        maxlen = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                inc+=1
                dec = 1
            elif nums[i+1] < nums[i]:
                dec += 1
                inc = 1
            else:
                inc =1
                dec = 1
            maxlen = max(maxlen,inc, dec)
        return maxlen
        
