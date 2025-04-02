class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        for i in range(len(strs)):
            a=list(strs[i])
            a.sort()
            l.append(''.join(a))
        s=set(l)
        res=[]
        for i in s:
            a=[]
            for j in range(len(l)):
                if i==l[j]:
                    a.append(strs[j])
            res.append(a)
        return res