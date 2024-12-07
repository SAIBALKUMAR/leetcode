class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        numRequired = 0

        for num in nums:
            if count == 0:
                numRequired = num
            
            if num == numRequired:
                count += 1
            else:
                count -=1
        
        return numRequired