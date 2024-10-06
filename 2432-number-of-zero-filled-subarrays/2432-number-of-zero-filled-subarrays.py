class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        prev_count = 0
        sub_arrays = 0
        for i in nums:
            if (i == 0):
                prev_count += 1
                sub_arrays += prev_count
            else:
                prev_count = 0
        return sub_arrays