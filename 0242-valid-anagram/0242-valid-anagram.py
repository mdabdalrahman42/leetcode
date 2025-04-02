class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        str1 = []
        str2 = []
        for i in range(len(s)):
            str1.append(s[i])
            str2.append(t[i])
        str1.sort()
        str2.sort()
        if str1 != str2:
            return False
        return True