class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanum(i):
            return (ord("0") <= ord(i) <= ord("9")) or (ord("A") <= ord(i) <= ord("Z")) or (ord("a") <= ord(i) <= ord("z"))

        l, r = 0, len(s) - 1
        while l <= r:
            while l < r and not isalphanum(s[l]):
                l += 1
            while l < r and not isalphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True