# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0
        queue = deque([[root, 1, 0]])
        curr_level = 0
        level_start = 1
        while queue:
            node, heap_val, level = queue.popleft()
            if level > curr_level:
                curr_level = level
                level_start = heap_val
            if node.left:
                queue.append([node.left, 2 * heap_val, level + 1])
            if node.right:
                queue.append([node.right, 2 * heap_val + 1, level + 1])
            max_dia = max(max_dia, heap_val - level_start + 1)
        return max_dia