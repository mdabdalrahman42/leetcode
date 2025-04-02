class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord("a")] += 1
            if tuple(count) not in dic:
                dic[tuple(count)] = []
            dic[tuple(count)].append(string)
        return list(dic.values())