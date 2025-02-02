# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == q:
            return p
        return self.funct(root, p, q)
    
    def funct(self, node, p, q):
        if (p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val):
            return node
        elif p.val < node.val and q.val < node.val:
            return self.funct(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            return self.funct(node.right, p, q)
        elif p == node:
            return p
        elif q == node:
            return q