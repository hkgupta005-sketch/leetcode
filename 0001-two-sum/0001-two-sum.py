class Solution(object):
    nums = [2,7,11,15]
    target = 9
    def twoSum(self, nums, target):
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if i!=j and num1+num2 == target:
                    return[i,j]
       