# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        last = head
        l = 1
        while last.next:
            last = last.next
            l += 1
        k = k % l
        if k == 0:
            return head
        curr = head
        for _ in range(l - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        last.next = head
        return new_head