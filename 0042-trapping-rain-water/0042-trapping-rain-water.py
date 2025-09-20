class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL < maxR:
                if maxL - height[l] > 0:
                    res += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])

            else:
                if maxR - height[r] > 0:
                    res += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])
        return res