class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        resLength = 0
        hashmapSum = {0:-1}
        prevSum = 0
        nums = [-1 if num == 0 else 1 for num in nums]
        for index, num in enumerate(nums):
            requiredSum = prevSum + num
            if requiredSum in hashmapSum:
                resLength = max(index - hashmapSum[requiredSum],resLength)
            else:
                hashmapSum[requiredSum] = index
            prevSum = requiredSum
        return resLength