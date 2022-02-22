# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        freq = defaultdict(int)
        freq[0] = 1
        self.count = 0

        def dfs(node, currentSum):
            if not node:
                return

            currentSum += node.val
            temp = currentSum - targetSum # the logic

            if temp in freq:
                self.count += freq[temp]

            freq[currentSum] += 1
            dfs(node.left, currentSum)
            dfs(node.right, currentSum)
            freq[currentSum] -= 1 # decrease the freq since we have gone thru that path

        dfs(root, 0)
        return self.count