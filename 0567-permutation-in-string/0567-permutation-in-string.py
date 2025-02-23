class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_char = [0] * 26
        s2_char = [0] * 26
        
        # Initialize frequency counts for s1 and first window in s2
        for i in range(len(s1)):
            s1_char[ord(s1[i]) - ord("a")] += 1
            s2_char[ord(s2[i]) - ord("a")] += 1

        # Count initial matches
        matches = sum(1 for i in range(26) if s1_char[i] == s2_char[i])
        
        l = 0  # Left pointer for sliding window
        for r in range(len(s1), len(s2)):  
            if matches == 26:
                return True

            # Add new character to window
            index = ord(s2[r]) - ord("a")
            s2_char[index] += 1
            if s2_char[index] == s1_char[index]:  
                matches += 1
            elif s2_char[index] == s1_char[index] + 1:  
                matches -= 1  # Over-counted

            # Remove old character from window
            rem_index = ord(s2[l]) - ord("a")
            s2_char[rem_index] -= 1
            if s2_char[rem_index] == s1_char[rem_index]:  
                matches += 1
            elif s2_char[rem_index] == s1_char[rem_index] - 1:  
                matches -= 1  # Under-counted

            l += 1  # Move left pointer

        # Final check for the last window
        return matches == 26
