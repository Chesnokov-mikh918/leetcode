# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        list_n = []
        def preorder_help(root: TreeNode | None, list_n: List[int]):
            if root is None:
                return

            list_n.append(root.val)
            preorder_help(root.left, list_n)
            preorder_help(root.right, list_n)
            return

        preorder_help(root, list_n)
        return list_n
        
        