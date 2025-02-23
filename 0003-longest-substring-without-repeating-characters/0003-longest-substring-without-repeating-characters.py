class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = 0
        output = 0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            output = max(output, r - l + 1)
        return output