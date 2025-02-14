# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        curr_level = 0
        level_low = 1
        queue = deque([(root, 1, 0)])
        while queue:
            node, val, level = queue.popleft()
            if level > curr_level:
                curr_level = level
                level_low = val
            max_width = max(max_width, val - level_low + 1)
            if node.left:
                queue.append((node.left, 2 * val, level + 1))
            if node.right:
                queue.append((node.right, 2 * val + 1, level + 1))
        return max_width