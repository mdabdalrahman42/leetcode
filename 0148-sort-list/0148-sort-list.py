# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def getMerge(left, right):
            dummy = ListNode()
            curr = dummy
            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            if left:
                curr.next = left
            if right:
                curr.next = right
            return dummy.next

        def getMid(l):
            slow, fast = l, l.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        if not head or not head.next:
            return head
        left = head
        mid = getMid(head)
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        return getMerge(left, right)