# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = deque([(root, 1, 0)])
        curr_level = 0
        low_val = 1
        while queue:
            node, val, level = queue.popleft()
            if node:
                if level > curr_level:
                    curr_level = level
                    low_val = val
                max_width = max(max_width, val - low_val + 1)
                queue.append((node.left, 2 * val, level + 1))
                queue.append((node.right, 2 * val + 1, level + 1))
        return max_width