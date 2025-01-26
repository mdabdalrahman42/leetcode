class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        else:
            output = []
            for i in range(m):
                output.append([original[j] for j in range(n * i, n + n * i)])
            return output