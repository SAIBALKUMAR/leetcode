class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        operations = 0
        nums.sort()

        mid = len(nums)//2

        if nums[mid] > k:
            operations += abs(k - nums[mid])
            nums[mid] = k

            index = mid-1
            while index >= 0 and nums[index] > nums[mid]:
                operations += abs(nums[index] - nums[mid])
                index -=1
        else:
            operations += abs(nums[mid] - k)
            nums[mid] = k

            index = mid + 1
            while index < len(nums) and nums[index] < nums[mid]:
                operations += abs(nums[mid] - nums[index])
                index += 1

        return operations