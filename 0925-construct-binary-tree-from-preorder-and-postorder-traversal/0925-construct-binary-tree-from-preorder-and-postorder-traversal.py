# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        length_of_array = len(postorder)
        dict_of_postorder = {}

        for i, n in enumerate(postorder):
            dict_of_postorder[n] = i

        def build(i1, i2, j1):
            if i1 > i2:
                return None
            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_value = preorder[i1+1]

                mid = dict_of_postorder[left_value]

                left_size = mid - j1 + 1

                root.left = build(i1 + 1, i1 + left_size, j1)
                root.right = build(i1 + left_size +1, i2, mid+1)
            return root
        
        return build(0, length_of_array-1, 0)
