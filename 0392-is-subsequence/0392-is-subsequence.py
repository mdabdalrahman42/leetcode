class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        ind = 0
        for i in t:
            if i == s[ind]:
                ind += 1
                if ind == len(s):
                    return True
        return False
        