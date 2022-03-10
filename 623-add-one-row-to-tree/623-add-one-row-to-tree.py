# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        def godown(root,dep):
            if root is None:
                return 
            if depth-1==dep:
                if root.left:
                    temp=root.left
                    root.left=TreeNode(val,temp,None)
                else:
                    root.left=TreeNode(val)
                if root.right:
                    temp=root.right
                    root.right=TreeNode(val,None,temp)
                else:
                    root.right=TreeNode(val)
                return
            if root.left:
                godown(root.left,dep+1)
            if root.right:
                godown(root.right,dep+1)
            return 
        if depth ==1:
            temp=root
            root=TreeNode(val,temp,None)
        else:
            godown(root,1)
        return root
                
                
                
                
                    
                    