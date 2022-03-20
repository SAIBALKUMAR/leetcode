# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minDiff=10000
        res=[]
        def inordertraversal(root):
            if root is None:
                return
            if root.left:
                inordertraversal(root.left)
             
            res.append(root.val)
            
            if root.right:
                inordertraversal(root.right)
        inordertraversal(root) 
        for i in range(len(res)-1):
            minDiff = min(abs(res[i+1]-res[i]),minDiff)
        
        return minDiff