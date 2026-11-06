# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        res = []
        def inorder_traversal(root: TreeNode | None):
            if root is None:
                return
            
            inorder_traversal(root.left)
            res.append(root.val)
            inorder_traversal(root.right)

        inorder_traversal(root)

        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True
            