class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=set()
        def backtrack(start,cur):
            if len(cur)>1:
                ans.add(tuple(cur))
            last = cur[-1] if cur else -100
            
            for i in range(start, n):
                if nums[i] >= last:
                    cur.append(nums[i])
                    backtrack(i+1,cur)
                    cur.pop()
            
        n=len(nums)
        backtrack(0,[])
        return ans
            
                