# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(node, curr_sum, path):
            curr_sum += node.val
            path = path + [node.val]
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    paths.append(path)
                    return
            if node.left:
                dfs(node.left, curr_sum, path)
            if node.right:
                dfs(node.right, curr_sum, path)
        if root:
            dfs(root, 0, [])
        return paths