# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        result=0
        def findhead(root,head):
            if head is None:
                return True
            if root is None:
                return False
            if root.val==head.val and check(root,head):
                return True    
            return findhead(root.left,head) or findhead(root.right,head)
            
        
        def check(root,head):
            if head is None:
                return True
            if root is None:
                return False
            if head.val == root.val:
                return (check(root.left,head.next)) or (check(root.right,head.next))
            return False
        
        return findhead(root,head)
        
                