# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        indexes = dict()
        for i in range(len(nums)):
            indexes[nums[i]] = i

        def bst_create(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            max_ind = indexes[max(nums[left:right + 1])]
            new_node = TreeNode(nums[max_ind])
            new_node.left = bst_create(left, max_ind - 1)
            new_node.right = bst_create(max_ind + 1, right)
            return new_node

        root = bst_create(0, len(nums) - 1)
        return root