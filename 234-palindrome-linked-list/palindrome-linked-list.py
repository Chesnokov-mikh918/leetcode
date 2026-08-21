# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        fast = head
        slow = head
        while fast != None and fast.next != None:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        if fast != None:
            slow = slow.next
        
        while slow != None:
            if (stack.pop() != slow.val):
                return False
            slow = slow.next
        return True


        