class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for num in range(n + 1):
            i = num
            while num:
                ans[i] += num % 2
                num = num // 2
        return ans