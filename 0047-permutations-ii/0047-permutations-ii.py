class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        tempPerm = []
        count = {n:0 for n in nums}
        for n in nums: 
            count[n] += 1
        
        def dfs():
            if (len(nums) == len(tempPerm)):
                res.append(tempPerm.copy())
                return
            
            for n in count:
                if (count[n] >0):
                    tempPerm.append(n)
                    count[n] -= 1

                    dfs()

                    tempPerm.pop()
                    count[n] += 1
        
        dfs()
        return res

            

        