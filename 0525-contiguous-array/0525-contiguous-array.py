class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        resLength = 0
        hashmapSum = {0:-1}
        requiredSum = 0
        for index, num in enumerate(nums):
            requiredSum += 1 if num == 1 else -1
            if requiredSum in hashmapSum:
                resLength = max(index - hashmapSum[requiredSum],resLength)
            else:
                hashmapSum[requiredSum] = index
        return resLength