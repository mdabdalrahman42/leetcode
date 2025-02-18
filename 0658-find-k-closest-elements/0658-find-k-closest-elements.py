class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        abs_sorted = sorted([(abs(x - i), i) for i in arr])
        k_nearest = abs_sorted[:k]
        return sorted([i[1] for i in k_nearest])