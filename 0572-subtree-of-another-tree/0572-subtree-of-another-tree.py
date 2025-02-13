# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        def check(node1, node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (node2 and not node1):
                return False
            if node1.val != node2.val:
                return False
            if not check(node1.left, node2.left) or not check(node1.right, node2.right):
                return False
            return True
        return check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)