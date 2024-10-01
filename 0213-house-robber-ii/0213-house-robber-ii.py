class Solution:
    def rob(self, nums: List[int]) -> int: 
        return max(nums[0], self.calculateMax(nums[1:]), self.calculateMax(nums[:-1]))


    def calculateMax(self,nums):
        max1, max2 = 0, 0
        for n in nums:
            newmax = max(max1+n, max2)
            max1 = max2
            max2 = newmax
        return max2