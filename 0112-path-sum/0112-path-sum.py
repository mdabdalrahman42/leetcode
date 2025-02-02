# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root != None:
            return self.dfs(root, targetSum, 0)
        return False

    def dfs(self, node, target, curr_sum):
        if node.left == None and node.right == None:
            if curr_sum + node.val == target:
                return True
            else:
                return False
        if node.left != None:
            if self.dfs(node.left, target, curr_sum + node.val):
                return True
            elif node.right != None:
                if self.dfs(node.right, target, curr_sum + node.val):
                    return True
        if node.right != None:
            if self.dfs(node.right, target, curr_sum + node.val):
                return True
        return False