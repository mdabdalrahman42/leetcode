class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        from collections import Counter

        dic1 = Counter(s)
        dic2 = Counter(t)

        if dic1 == dic2:
            return True
        
        return False