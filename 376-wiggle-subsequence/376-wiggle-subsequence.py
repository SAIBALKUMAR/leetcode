class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        inc =[1]*n
        dec=[1]*n
        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j] and inc[i]<dec[j]+1:
                    inc[i]=dec[j]+1
                if nums[i]<nums[j] and dec[i]<inc[j]+1:
                    dec[i]=inc[j]+1
        return max(max(dec),max(inc))

                    