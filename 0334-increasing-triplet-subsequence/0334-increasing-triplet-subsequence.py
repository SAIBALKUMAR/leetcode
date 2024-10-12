class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if (len(nums) < 3):
            return False
        minimumNumber = {
            'min': 2**31,     # Maximum value for a 32-bit signed integer
            'pattern': []
        }
        for i in range(0,len(nums)):
            if (nums[i] < minimumNumber['min']):
                minimumNumber['min'] = nums[i]
            elif (nums[i] > minimumNumber['min']):
                if (len(minimumNumber['pattern']) > 0):
                    if (minimumNumber['pattern'][0][1] > nums[i]): 
                        minimumNumber['pattern'] = [[minimumNumber['min'], nums[i]]]
                    elif (minimumNumber['pattern'][0][1] < nums[i]):
                        return True
                else:
                    minimumNumber['pattern'] = [[minimumNumber['min'], nums[i]]]
        return False
