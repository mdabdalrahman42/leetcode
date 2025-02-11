# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        dic = {}
        def dfs1(node):
            if node.left:
                if node in dic:
                    dic[node].append(node.left)
                else:
                    dic[node] = [node.left]
                if node.left in dic:
                    dic[node.left].append(node)
                else:
                    dic[node.left] = [node]
                dfs1(node.left)
            if node.right:
                if node in dic:
                    dic[node].append(node.right)
                else:
                    dic[node] = [node.right]
                if node.right in dic:
                    dic[node.right].append(node)
                else:
                    dic[node.right] = [node]
                dfs1(node.right)
            if not node.left and not node.right:
                if node not in dic:
                    dic[node] = []
        dfs1(root)
        output = []
        visited = set()
        visited.add(target)
        queue = deque([(target, 0)])
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                output.append(node.val)
            else:
                for v in dic[node]:
                    if v not in visited:
                        visited.add(v)
                        queue.append((v, distance + 1))
        return output
            