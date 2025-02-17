class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bot = rows - 1
        while top <= bot:
            mid = top + (bot - top) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][cols - 1]:
                top = mid + 1
            else:
                break
        if not top <= bot:
            return False
        row = top + (bot - top) // 2
        l = 0
        r = cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                r = mid - 1
            if matrix[row][mid] < target:
                l = mid + 1
        return False