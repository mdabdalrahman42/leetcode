# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q or (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val):
            return root
        elif root.val > p.val and root.val > q.val:
            l = self.lowestCommonAncestor(root.left, p, q)
            r = None
        elif root.val < p.val and root.val < q.val:
            r = self.lowestCommonAncestor(root.right, p, q)
            l = None
        if l:
            return l
        elif r:
            return r