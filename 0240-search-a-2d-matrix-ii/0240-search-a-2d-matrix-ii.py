class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        r, c = 0, cols - 1
        while r < rows and c >= 0:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
        return False