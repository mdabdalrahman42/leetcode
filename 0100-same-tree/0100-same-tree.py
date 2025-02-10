# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(n1, n2):
            if n1 and n2:
                if n1.val == n2.val:
                    if dfs(n1.left, n2.left) and dfs(n1.right, n2.right):
                        return True
                    else:
                        return False
                else:
                    return False
            elif not n1 or not n2:
                if n1 == n2:
                    return True
                else:
                    return False
        return dfs(p, q)