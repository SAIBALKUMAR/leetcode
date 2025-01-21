class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        num_length = len(nums)
        i =0
        for i in range(num_length):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            
            target = nums[i] + k
            left, right = i+1,num_length - 1

            while left <= right:
                mid = (left + right)//2
                if (target == nums[mid]):
                    res += 1
                    break
                elif target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            
        return res