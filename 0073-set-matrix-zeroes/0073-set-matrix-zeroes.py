class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
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
        """
        row_1 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0:
                    if matrix[i][j] == 0:
                        row_1 = 0
                else:
                    if matrix[i][j] == 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[i])):
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(1, len(matrix)):
                matrix[i][0] = 0
        if row_1 == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0