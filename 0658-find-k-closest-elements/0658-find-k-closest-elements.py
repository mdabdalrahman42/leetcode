class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        abs_diff = [(abs(x - i), i) for i in arr]
        sorted_abs_diff = sorted(abs_diff)
        k_nearest = sorted_abs_diff[:k]
        return sorted([i[1] for i in k_nearest])