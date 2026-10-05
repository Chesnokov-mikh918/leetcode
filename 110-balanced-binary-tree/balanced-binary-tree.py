# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
is_balanced = True

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def get_height(root: TreeNode | None):
            if root is None:
                return 0

            height_right = get_height(root.right)
            height_left = get_height(root.left)

            if height_right == -1 or height_left == -1:
                return -1

            if abs(height_right - height_left) > 1:
                return -1
            
            return 1 + max(height_right, height_left)
        
        return get_height(root) != -1