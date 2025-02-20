# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        last_node = curr
        k = k % length
        if k == length or k == 0:
            return head
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        last_node.next = head
        return new_head