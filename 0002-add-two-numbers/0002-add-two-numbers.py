# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0 ,None)
        carry = 0
        tail = dummy
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + carry
            carry = v // 10
            tail.next = ListNode(v % 10, None)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            tail.next = ListNode(carry, None)
            tail = tail.next
        return dummy.next