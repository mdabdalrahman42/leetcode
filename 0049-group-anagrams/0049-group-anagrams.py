class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for string in strs:
            dummy = []
            for s in string:
                dummy.append(s)
            dummy.sort()
            sorted_strs.append(''.join(dummy))
        no_dup = set(sorted_strs)
        output = []
        for string in no_dup:
            anagrams = []
            for i in range(len(sorted_strs)):
                if string == sorted_strs[i]:
                    anagrams.append(strs[i])
            output.append(anagrams)
        return output