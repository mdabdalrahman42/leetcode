# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(t1, t2):
            if not t1 and not t2:
                return True
            if (t1 and not t2) or (t2 and not t1):
                return False
            if t1.val != t2.val:
                return False
            if not compare(t1.left, t2.left):
                return False
            if not compare(t1.right, t2.right):
                return False
            return True
        
        if not root:
            return False
        if compare(root, subRoot): 
            return True
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True
        return False