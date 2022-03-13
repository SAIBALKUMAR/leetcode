class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return 0
        
        
        
        def check(num):
            if num[1]-num[0]==num[2]-num[1]:
                return True
            else:
                return False
        startidx=0
        dp=[0]*len(nums)
        for i in range(2,len(nums)):
            if check(nums[startidx:i+3]):
                dp[i]=dp[i-1]+1
            startidx+=1
        
        return sum(dp)
        
        
                
            