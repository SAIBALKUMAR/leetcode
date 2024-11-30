class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for j in range(1, len(nums)):
            if (nums[j] != nums[index -1]):
                nums[index] = nums[j]
                index += 1
        return index