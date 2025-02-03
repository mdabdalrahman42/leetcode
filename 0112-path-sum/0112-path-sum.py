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
            if node.left == None and node.right == None:
                if curr_sum == targetSum:
                    return True
                else:
                    return False
            if node.left != None:
                if dfs(node.left, curr_sum):
                    return True
            if node.right != None:
                if dfs(node.right, curr_sum):
                    return True
            return False

        if root == None:
            return False

        if dfs(root, 0):
            return True
        return False