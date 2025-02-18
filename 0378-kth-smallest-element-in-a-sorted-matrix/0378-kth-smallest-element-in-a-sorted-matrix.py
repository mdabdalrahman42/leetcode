class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        l, r = matrix[0][0], matrix[-1][-1]
        
        def count(num):
            cnt = 0
            for row in matrix:
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if num > row[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
                cnt += l
            return cnt

        while l <= r:
            mid = l + (r - l) // 2
            if count(mid) < k:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1