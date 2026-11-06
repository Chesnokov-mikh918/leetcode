# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.ans = 0
        self.count = 0
        def inorder(root):
            if root is None:
                return False
            
            if inorder(root.left):
                return True

            self.count += 1
            if self.count == k:
                self.ans = root.val
                return True

            if inorder(root.right):
                return True

        inorder(root)
        return self.ans