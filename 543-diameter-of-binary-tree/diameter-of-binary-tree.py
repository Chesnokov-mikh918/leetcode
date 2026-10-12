# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def find_max_len(root: TreeNode | None):
            nonlocal max_len
            if root is None:
                return 0

            left_len = find_max_len(root.left)
            right_len = find_max_len(root.right)
            max_len = max(max_len, left_len + right_len)

            return max(left_len, right_len) + 1

        find_max_len(root)
        return max_len
