# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            next_set = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = next_set
            prev = curr
            curr = next_set

        return dummy.next