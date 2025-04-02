class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = 1
            else:
                dic1[i] += 1
        for i in t:
            if i not in dic2:
                dic2[i] = 1
            else:
                dic2[i] += 1
        return dic1 == dic2