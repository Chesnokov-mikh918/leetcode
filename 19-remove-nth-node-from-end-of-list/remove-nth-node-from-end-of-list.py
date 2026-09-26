# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        first = head
        second = head
        count = n
        prev = None

        while count > 0:
            first = first.next
            count -= 1
        
        while first != None:
            first = first.next
            prev = second
            second = second.next

        if second == head:
            return head.next

        prev.next = second.next
        return head