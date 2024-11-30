class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1Index = m - 1
        num2Index = n - 1
        right = m + n - 1
        while num2Index >= 0:
            if (num1Index >= 0 and nums1[num1Index] > nums2[num2Index]):
                nums1[right] = nums1[num1Index]
                num1Index -= 1
            else:
                nums1[right] = nums2[num2Index]
                num2Index -= 1
            right -= 1