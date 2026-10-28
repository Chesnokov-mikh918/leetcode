# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []
        deq = deque([root])
        while deq:
            len_deq = len(deq)
            new_level = []
            for i in range(len_deq):
                el = deq.popleft()
                if el is not None:
                    deq.append(el.left)
                    deq.append(el.right)
                    new_level.append(el.val)
            if new_level:
                ans.append(new_level)
        return ans
