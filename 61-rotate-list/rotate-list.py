# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def count_len_and_makecycle(head: ListNode | None) -> int:
    cur = head
    count = 1
    while cur.next is not None:
        count += 1
        cur = cur.next
    cur.next = head
    return count

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return 

        len_arr = count_len_and_makecycle(head)
        
        r = k % len_arr
        new_tail = head
        for i in range(len_arr - r - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head