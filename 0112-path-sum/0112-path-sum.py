# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            curr_sum += node.val
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True
            if node.left:
                if dfs(node.left, curr_sum):
                    return True
            if node.right:
                if dfs(node.right, curr_sum):
                    return True
            return False
        if root:
            return dfs(root, 0)
        return False