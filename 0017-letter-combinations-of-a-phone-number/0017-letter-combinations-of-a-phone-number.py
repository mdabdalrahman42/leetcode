class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}
        res = []
        def dfs(i, comb):
            if len(comb) == len(digits):
                res.append(comb)
                return
            for j in letters[digits[i]]:
                dfs(i + 1, comb + j)
        if digits:
            dfs(0, "")
        return res
