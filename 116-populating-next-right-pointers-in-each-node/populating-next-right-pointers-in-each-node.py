"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])
        while q:
            last = None
            for i in range(len(q)):
                node = q.pop()
                if node:
                    q.appendleft(node.right)
                    q.appendleft(node.left)
                    node.next = last
                last = node
        return root
                
                

        