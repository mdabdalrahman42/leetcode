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
        level = 0
        low_val = 1
        while queue:
            node, curr_val, curr_level = queue.popleft()
            if curr_level > level:
                level = curr_level
                low_val = curr_val
            if node.left:
                queue.append((node.left, 2 * curr_val, curr_level + 1))
            if node.right:
                queue.append((node.right, 2 * curr_val + 1, curr_level + 1))
            max_width = max(max_width, curr_val - low_val + 1)
        return max_width