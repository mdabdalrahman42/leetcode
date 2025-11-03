class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        lo, hi = matrix[0][0], matrix[-1][-1]  # value range

        def count_le(x):  # count of elements <= x
            total = 0
            for row in matrix:
                total += bisect_right(row, x)
            return total

        # Find smallest x such that count_le(x) >= k
        while lo <= hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo