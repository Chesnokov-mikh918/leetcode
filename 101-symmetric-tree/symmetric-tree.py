# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def my_simm(left, right):
            if left is None and right is None:
                return True
            if left is None and right is not None or left is not None and right is None:
                return False
            return left.val == right.val and my_simm(left.right, right.left) and my_simm(left.left, right.right)

        if root is None:
            return True
        
        return my_simm(root.left, root.right)