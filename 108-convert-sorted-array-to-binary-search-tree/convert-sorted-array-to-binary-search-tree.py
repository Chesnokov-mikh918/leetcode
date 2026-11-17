# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def bst_create(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            mid = (left + right) // 2
            new_node = TreeNode(nums[mid])
            new_node.left = bst_create(left, mid - 1)
            new_node.right = bst_create(mid + 1, right)
            return new_node

        root = bst_create(0, len(nums) - 1)
        return root