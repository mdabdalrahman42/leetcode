# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        dic = {0:1}
        def path(node, curr_sum):
            nonlocal count
            curr_sum += node.val
            if curr_sum - targetSum in dic:
                count += dic[curr_sum - targetSum]
            if curr_sum in dic:
                dic[curr_sum] += 1
            else:
                dic[curr_sum] = 1
            if node.left:
                path(node.left, curr_sum)
            if node.right:
                path(node.right, curr_sum)
            if dic[curr_sum] == 1:
                dic.pop(curr_sum)
            else:
                dic[curr_sum] -= 1
        if root:
            path(root, 0)
        return count