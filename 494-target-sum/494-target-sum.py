class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
#         res=[]
#         def check(nums,target,sumi):
#             if len(nums)==1:
#                 if sumi+nums[0]==target:
#                     res.append(1)
#                 if sumi-nums[0]==target:
#                     res.append(1)
#                 return
            
#             check(nums[1:],target,sumi+nums[0])
#             check(nums[1:],target,sumi-nums[0])
        
#         check(nums,target,0)
#         return sum(res)

        dp={}
         
        def backtrack(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = (backtrack(i+1, total + nums[i]) + backtrack(i+1,total-nums[i]))
            
            return dp[(i,total)]
        
        return backtrack(0,0)