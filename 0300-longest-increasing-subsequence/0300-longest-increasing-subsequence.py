class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        indices = [None for x in range(len(nums) +1)]
        length = 0
        for i, num in enumerate(nums):
            updated_length = self.binarySearch(1, length, indices, nums, num)
            indices[updated_length] = i
            length = max(updated_length, length)
        return length
        
    def binarySearch(self, start_index, end_index, indices, nums,num):
        if start_index> end_index:
            return start_index
        
        middle_index = (start_index + end_index) // 2

        if nums[indices[middle_index]] < num:
            start_index = middle_index + 1
        else:
            end_index = middle_index - 1

        return self.binarySearch(start_index, end_index, indices, nums,num)
    