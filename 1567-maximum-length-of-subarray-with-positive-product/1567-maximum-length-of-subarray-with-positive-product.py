class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        i = j = output = 0
        curr = 1
        for idx, num in enumerate(nums):
            if not num:
                i = j = idx + 1
                curr = 1
            else:
                if num < 0 and i == j:
                    j = idx + 1
                    
                curr /= 1 if num > 0 else -1
                if curr > 0:
                    output = max(output, idx - i + 1)
                else:
                    output = max(output, idx - j + 1)
                    
        return output