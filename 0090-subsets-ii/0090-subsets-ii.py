class Solution:
    def dfs(self,nums,path,res):
        res.append(path)
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            self.dfs(nums[i+1:], path+[nums[i]], res)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        self.dfs(nums,[],res)
        return res