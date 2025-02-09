class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [1 for i in range(len(matrix))]
        cols = [1 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0
        for i in range(len(rows)):
            if rows[i] == 0:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        for j in range(len(cols)):
            if cols[j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0