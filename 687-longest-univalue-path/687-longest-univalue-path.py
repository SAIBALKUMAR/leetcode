# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxLen = 0
        
        def dfs(node):
            
            nonlocal maxLen
            if not node.left and not node.right:
                return 0
            
            wide = 0
            currentDepth = 0
            
            if node.left:
                leftDepth = dfs(node.left)
                if node.left.val == node.val:
                    wide += 1 + leftDepth
                    currentDepth = max(currentDepth, 1+leftDepth)
                    
            if node.right:
                rightDepth = dfs(node.right)
                if node.right.val == node.val:
                    wide += 1 + rightDepth
                    currentDepth = max(currentDepth, 1+rightDepth)
                
            maxLen = max(maxLen, wide, currentDepth)
            
            return currentDepth
        
        if root:
            dfs(root)
            
        return maxLen