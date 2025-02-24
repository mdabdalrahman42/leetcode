class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lng = 0
        l = 0
        visited = set()
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            lng = max(lng, r - l + 1)
        return lng