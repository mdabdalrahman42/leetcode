# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = {0: 1}
        count = 0
        def dfs(node, curr_sum):
            nonlocal count
            curr_sum += node.val
            if curr_sum - targetSum in dic:
                count += dic[curr_sum - targetSum]
            if curr_sum not in dic:
                dic[curr_sum] = 1
            else:
                dic[curr_sum] += 1
            if node.left:
                dfs(node.left, curr_sum)
            if node.right:
                dfs(node.right, curr_sum)
            if dic[curr_sum] == 1:
                dic.pop(curr_sum)
            else:
                dic[curr_sum] -= 1
        if root:
            dfs(root, 0)
        return count
            