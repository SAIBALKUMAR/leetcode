class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        leftIndex = 0
        total = 0
        for rightIndex in range(len(nums)):
            total += nums[rightIndex]
            while total >= target:
                result = min(rightIndex-leftIndex+1, result)
                total -= nums[leftIndex]
                leftIndex+=1
            
        return 0 if result == float("inf") else result
        
            
            
