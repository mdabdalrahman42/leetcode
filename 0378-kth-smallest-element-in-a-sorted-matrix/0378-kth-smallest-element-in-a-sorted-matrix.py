class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]

        def cnt(num):
            count = 0
            for row in matrix:
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if num > row[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
                count += l
            return count

        while l <= r:
            mid = l + (r - l) // 2
            if cnt(mid) < k:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1