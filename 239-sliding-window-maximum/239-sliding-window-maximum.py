class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = right = 0
        queue = collections.deque()
        
        while right < len(nums):
            # removing all those values from queue which is less than new value in window
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            # removing queue max value if it is less than left
            if queue[0] < left:
                queue.popleft()
            
            if (right + 1 >= k):
                result.append(nums[queue[0]])
                left +=1
            right +=1
        return result
                
                
            