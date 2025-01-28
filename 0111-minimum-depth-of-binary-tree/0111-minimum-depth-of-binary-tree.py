# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        queue = []
        if root != None:
            queue.insert(0, root)
        else:
            return depth
        while queue:
            depth += 1
            l = len(queue)
            for _ in range(l):
                node = queue.pop()
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
                if not node.left and not node.right:
                    return depth