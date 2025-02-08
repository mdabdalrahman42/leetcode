class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            t, b = l, r
            for i in range(r - l):
                temp = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = temp
            l += 1
            r -= 1
        """
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        for i in range(len(matrix)):
            matrix[i].reverse()