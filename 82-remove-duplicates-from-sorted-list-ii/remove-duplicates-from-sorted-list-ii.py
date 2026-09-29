# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        cur = head
        prev = None
        while cur is not None and cur.next is not None:
            if cur.next.val == cur.val:
                bad_val = cur.val
                while cur is not None and cur.val == bad_val:
                    cur = cur.next
                if not prev:
                    head = cur
                else:
                    prev.next = cur
            else:
                cur, prev = cur.next, cur
        return head