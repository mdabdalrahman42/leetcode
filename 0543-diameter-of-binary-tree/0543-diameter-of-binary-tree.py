# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(n):
            nonlocal longest
            if not n:
                return 0
            left = dfs(n.left)
            right = dfs(n.right)
            longest = max(longest, left + right)
            return 1 + max(left, right)
        dfs(root)
        return longest