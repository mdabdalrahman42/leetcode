# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            next_pair = curr.next.next
            temp = curr.next
            curr.next.next = curr
            prev.next = temp
            curr.next = next_pair
            prev = curr
            curr = next_pair
        return dummy.next 