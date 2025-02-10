# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(n, length):
            nonlocal longest
            length += 1
            if not n.left and not n.right:
                longest = max(longest, length)
            else:
                if n.left:
                    dfs(n.left, length)
                if n.right:
                    dfs(n.right, length)
        if root:
            dfs(root, 0)
        return longest