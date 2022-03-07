class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def find_gcd(x, y):
            while(y):
                x, y = y, x % y

            return x
        if len(nums)<2:
            return nums==[1]
        num1=nums[0]
        num2=nums[1]
        gcd=find_gcd(num1,num2)
        for i in range(2,len(nums)):
            gcd=find_gcd(gcd,nums[i])
        return gcd==1