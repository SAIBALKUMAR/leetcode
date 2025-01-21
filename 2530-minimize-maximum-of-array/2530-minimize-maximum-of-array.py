class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            res = max(res, math.ceil(total/(i+1)))
        return res