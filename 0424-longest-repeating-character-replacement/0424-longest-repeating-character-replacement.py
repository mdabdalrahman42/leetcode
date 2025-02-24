class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_sub = 0
        freq = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            freq = max(freq, count[s[r]])
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            max_sub = max(max_sub, r - l + 1)
        return max_sub