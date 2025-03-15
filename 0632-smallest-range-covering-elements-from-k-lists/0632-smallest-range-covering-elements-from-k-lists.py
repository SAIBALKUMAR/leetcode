class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # create a min_heap and left and right
        # loop through nums and get left, right and min_heap
        min_heap = []
        left = right = nums[0][0]
        for i in range(len(nums)):
            element_array = nums[i]
            left = min(left, element_array[0])
            right = max(right, element_array[0])
            heapq.heappush(min_heap, (element_array[0], i , 0))
        
        result = [left, right]

        while True:
            value, i, idx = heapq.heappop(min_heap)
            idx += 1
            if (idx >= len(nums[i])):
                return result
            
            next_value = nums[i][idx]
            heapq.heappush(min_heap, (next_value, i, idx))
            right = max(right, next_value)
            left = min_heap[0][0]
            if (result[1] - result[0] > right - left):
                result = [left, right]
            
