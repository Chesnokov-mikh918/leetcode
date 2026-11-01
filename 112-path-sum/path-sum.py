# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def has_sum(root, sum):
            if root is None:
                return False
            sum += root.val
            if sum == targetSum and root.left is None and root.right is None:
                return True
            return has_sum(root.left, sum) or has_sum(root.right, sum)
        return has_sum(root, 0)