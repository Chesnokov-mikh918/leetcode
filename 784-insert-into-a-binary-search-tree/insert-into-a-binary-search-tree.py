# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # if root is None:
        #     return TreeNode(val)
        
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)

        # if root.val < val:
        #     root.right = self.insertIntoBST(root.right, val)
        
        # return root
        cur = root
        if cur is None:
            return TreeNode(val)
        while 1:
            if cur.val < val:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right

            if cur.val > val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            
        return root
        