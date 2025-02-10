# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node, sub):
            if not node and not sub:
                return True
            if (not node and sub) or (node and not sub): 
                return False
            if node.val == sub.val:
                if check(node.left, sub.left) and check(node.right, sub.right):
                    return True
            return False
        if not root:
            return False
        if check(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot): 
            return True
        if self.isSubtree(root.right, subRoot): 
            return True
        return False