class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_chars = [0] * 26
        s2_chars = [0] * 26
        for i in range(len(s1)):
            s1_chars[ord(s1[i]) - ord("a")] += 1
            s2_chars[ord(s2[i]) - ord("a")] += 1
        matches = 0
        for i in range(26):
            if s1_chars[i] == s2_chars[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord("a")
            s2_chars[index] += 1
            if s1_chars[index] == s2_chars[index]:
                matches += 1
            elif s2_chars[index] == s1_chars[index] + 1:
                matches -= 1
            index = ord(s2[l]) - ord("a")
            s2_chars[index] -= 1
            if s1_chars[index] == s2_chars[index]:
                matches += 1
            elif s2_chars[index] == s1_chars[index] - 1:
                matches -= 1
            l += 1
        return matches == 26