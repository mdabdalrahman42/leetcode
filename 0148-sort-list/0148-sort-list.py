# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def getMid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def getMerge(left, right):
            dummy = ListNode(0, None)
            tail = dummy
            while left and right:
                if left.val <= right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            if left:
                tail.next = left
            if right:
                tail.next = right
            return dummy.next

        if not head or not head.next:
            return head
        left = head
        mid = getMid(head)
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        return getMerge(left, right)