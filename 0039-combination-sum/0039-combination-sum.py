class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output=[]
        
        self.getCombinations(sorted(candidates),target,[],output)
        return output
    
    def getCombinations(self, candidates, target, cur, res):
        if target == 0:
            res.append(cur)
        if target < 0:
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            self.getCombinations(candidates[i:], target - candidates[i], cur+[candidates[i]], res)

        