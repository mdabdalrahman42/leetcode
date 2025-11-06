class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]

        res = n + 1
        for i in range(n):
            l, r = i, n - 1          # search mids in [i, n-1]
            best = n                  # store best mid; n means "not found"
            while l <= r:
                mid = (l + r) // 2
                curSum = P[mid + 1] - P[i]
                if curSum >= target:
                    best = mid        # potential answer; try to shrink
                    r = mid - 1       # <-- move left (bisect_left behavior)
                else:
                    l = mid + 1

            if best != n:
                res = min(res, best - i + 1)

        return 0 if res == n + 1 else res
