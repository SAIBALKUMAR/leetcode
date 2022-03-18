class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        
        def compare(n1,n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1
        res=sorted(nums,key=cmp_to_key(compare))
        return str(int("".join(res)))
            