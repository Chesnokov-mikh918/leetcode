# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        list_n = []
        def helpi(root, list_n):
            if root is None:
                return

            helpi(root.left, list_n)
            helpi(root.right, list_n)
            list_n.append(root.val)
            
            return

        helpi(root, list_n)
        return list_n