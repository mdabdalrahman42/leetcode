# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr = head, head.next
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return head
        