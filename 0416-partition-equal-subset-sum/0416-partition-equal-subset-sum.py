class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        visitSet = set()
        visitSet.add(0)
        target = sum(nums) // 2
        for i in range(len(nums)-1,-1,-1):
            dpSet = set()
            for num in visitSet:
                if (num + nums[i]) == target:
                    return True
                dpSet.add(num + nums[i])
                dpSet.add(num)
            visitSet = dpSet
            
        return True if target in visitSet else False
        