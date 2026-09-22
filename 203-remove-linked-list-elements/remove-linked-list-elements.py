# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head is None:
            return None
        dummy_head = ListNode()

        curr = head
        curr_dummy_head = dummy_head
        while curr is not None:
            if curr.val != val:
                curr_dummy_head.next = curr
                curr_dummy_head = curr_dummy_head.next
            curr = curr.next

        curr_dummy_head.next = None

        if dummy_head.next is None:
            return None

        return dummy_head.next