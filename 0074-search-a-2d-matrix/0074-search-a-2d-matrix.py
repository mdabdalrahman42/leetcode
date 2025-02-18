class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        while t <= b:
            mid = t + (b - t) // 2
            if target > matrix[mid][len(matrix[0]) - 1]:
                t = mid + 1
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                break
        if not t <= b:
            return False
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[mid][m] == target:
                return True
            elif target > matrix[mid][m]:
                l = m + 1
            else:
                r = m - 1
        return False