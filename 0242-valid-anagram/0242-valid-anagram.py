class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            dic1[s[i]] = 1 + dic1.get(s[i], 0)
            dic2[t[i]] = 1 + dic2.get(t[i], 0)
        return dic1 == dic2