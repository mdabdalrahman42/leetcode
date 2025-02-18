class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix) - 1, 0
        while r >= 0 and c < len(matrix[0]):
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                r -= 1
            elif target > matrix[r][c]:
                c += 1
        return False