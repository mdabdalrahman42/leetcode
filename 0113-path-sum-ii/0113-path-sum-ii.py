# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, curr_sum, path):
            curr_sum += node.val
            path = path + [node.val]
            if node.left == None and node.right == None:
                if curr_sum == targetSum:
                    paths.append(path)
            if node.left != None:
                dfs(node.left, curr_sum, path)
            if node.right != None:
                dfs(node.right, curr_sum, path)

        paths = []
        if root:
            dfs(root, 0, [])
        return paths