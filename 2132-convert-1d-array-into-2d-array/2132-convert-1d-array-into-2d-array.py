class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        output = []
        if m * n == len(original):
            for i in range(m):
                row = []
                for j in range(i*n , (i + 1) * n):
                    row.append(original[j])
                output.append(row)
        return output