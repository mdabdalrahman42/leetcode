# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            nonlocal count
            if node == None:
                return
            curr_sum += node.val
            if curr_sum - targetSum in dic:
                count += dic[curr_sum - targetSum]
            if curr_sum not in dic:
                dic[curr_sum] = 1
            else:
                dic[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            if dic[curr_sum] > 1:
                dic[curr_sum] -= 1
            else:
                dic.pop(curr_sum)
        dic = {0:1}
        count = 0
        dfs(root, 0)
        return count