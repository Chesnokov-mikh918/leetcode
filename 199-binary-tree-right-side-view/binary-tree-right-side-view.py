# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        deq = deque([root])
        ans = []
        while deq:
            len_deq = len(deq)
            ans.append(deq[-1].val)
            for i in range(len_deq):
                el = deq.popleft()
                if el is not None:
                    if el.left is not None:
                        deq.append(el.left)
                    if el.right is not None:
                        deq.append(el.right)
        return ans
                