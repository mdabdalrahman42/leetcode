# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(n, curr_sum):
            if n:
                curr_sum += n.val
                if not n.left and not n.right:
                    return curr_sum == targetSum
                if n.left:
                    if dfs(n.left, curr_sum):
                        return True
                if n.right:
                    if dfs(n.right, curr_sum):
                        return True
            return False 
        return dfs(root, 0)