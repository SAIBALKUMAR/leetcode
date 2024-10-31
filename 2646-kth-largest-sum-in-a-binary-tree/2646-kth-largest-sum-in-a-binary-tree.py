# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        queue.append(root)
        min_heap = []
        while queue:
            level_sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if (node.left):
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)
            heapq.heappush(min_heap, level_sum)
            if (len(min_heap) > k):
                heapq.heappop(min_heap)
        
        return -1 if len(min_heap) < k else min_heap[0]