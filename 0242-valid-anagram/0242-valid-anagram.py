class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        from collections import Counter

        dic1 = Counter(s)
        dic2 = Counter(t)

        if dic1 != dic2:
            return False
        
        return True