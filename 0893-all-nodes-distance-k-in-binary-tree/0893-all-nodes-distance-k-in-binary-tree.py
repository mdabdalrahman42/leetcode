# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dic = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node not in dic:
                dic[node] = []
            if node.left:
                if node.left not in dic:
                    dic[node.left] = []
                dic[node].append(node.left)
                dic[node.left].append(node)
                queue.append(node.left)
            if node.right:
                if node.right not in dic:
                    dic[node.right] = []
                dic[node].append(node.right)
                dic[node.right].append(node)
                queue.append(node.right)
        visited = set([target])
        output = []
        queue = deque([(target, 0)])
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                output.append(node.val)
            else:
                for adj_node in dic[node]:
                    if adj_node not in visited:
                        queue.append((adj_node, distance + 1))
                        visited.add(adj_node)
        return output