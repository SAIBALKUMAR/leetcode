class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # if (len(nums) == 0): return [[lower,upper]]
        # nums = [lower] + nums + [upper]
        # result_ranges = []
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i-1] > 1:
        #         result_ranges.append([nums[i-1]+1, nums[i]-1])
        # if (len(result_ranges) > 0 and result_ranges[-1][-1] < upper):
        #     result_ranges[-1][-1] = upper
        # return result_ranges
        result = []

        for num in nums + [upper + 1]:

            if num > lower:
                result.append([lower, num - 1])

            lower = num + 1
            
        
        return result