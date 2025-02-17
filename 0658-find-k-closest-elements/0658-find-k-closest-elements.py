class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if x > arr[mid]:
                l = mid + 1
            else:
                r = mid
        p1, p2 = l - 1, l
        while k > 0:
            if p1 < 0:
                p2 += 1
            elif p2 >= len(arr):
                p1 -= 1
            elif abs(x - arr[p1]) <= abs(arr[p2] - x):
                p1 -= 1
            else:
                p2 += 1
            k -= 1
        return arr[p1 + 1:p2]