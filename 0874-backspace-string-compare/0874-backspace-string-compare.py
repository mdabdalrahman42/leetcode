class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def valid(str, i):
            back_spaces = 0
            while i >= 0:
                if str[i] == "#":
                    back_spaces += 1
                elif str[i] != "#" and back_spaces == 0:
                    return i
                else:
                    back_spaces -= 1
                i -= 1
            return i
        
        ind_s, ind_t = len(s) - 1, len(t) - 1
        while ind_s >= 0 or ind_t >= 0:
            ind_s = valid(s, ind_s)
            ind_t = valid(t, ind_t)
            char_s = "" if ind_s < 0 else s[ind_s]
            char_t = "" if ind_t < 0 else t[ind_t]
            if char_s != char_t:
                return False
            ind_s -= 1
            ind_t -= 1
        return True