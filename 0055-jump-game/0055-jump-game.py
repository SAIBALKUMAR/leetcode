class Solution:
    def canJump(self, nums: List[int]) -> bool:
        required = 0
        available = 0
        for i in range(len(nums)):
            if (i > available):
                return False
            available = max(available, i + nums[i])
        return True

