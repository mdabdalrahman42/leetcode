class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        abs_diff = [(abs(x - i), i) for i in arr]
        sort_abs = sorted(abs_diff)
        nearest = [sort_abs[i][1] for i in range(k)]
        return sorted(nearest)