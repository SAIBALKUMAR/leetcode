"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root
        res=[]
        queue=[root,'n']
        while len(queue)>0:
            curr=queue.pop(0)
            if curr!='n':
                res.append(curr)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            elif curr =='n':
                if len(queue)==0:
                    break
                else:
                    queue.append('n')
                res.append('n')
        i=0
        while i<len(res)-1:
            if res[i+1]!='n':
                res[i].next=res[i+1]
            else:
                res[i].next=None
                i+=1
            i+=1
        return res[0]
                

            
            