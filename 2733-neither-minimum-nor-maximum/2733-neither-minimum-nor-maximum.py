class Solution(object):
    def findNonMinOrMax(self, nums):
        n = min(nums)
        k = max(nums)
        for i in nums:
            if i>n and i<k:
                return i
        return -1
        