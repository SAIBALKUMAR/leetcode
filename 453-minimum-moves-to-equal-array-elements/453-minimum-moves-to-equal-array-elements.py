class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=min(nums)
        res=0
        for i in range(len(nums)):
            res+=(nums[i]-mini)
        return res
                