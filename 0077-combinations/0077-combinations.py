class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums,k,path,res):
            if (len(path) == k):
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], k, path+ [nums[i]], res)

        res = []
        dfs(range(1,n+1), k, [],res)
        return res
