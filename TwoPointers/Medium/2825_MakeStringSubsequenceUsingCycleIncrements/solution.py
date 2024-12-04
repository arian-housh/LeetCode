class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0  # pointer for str1
        j = 0  # pointer for str2
        
        while i < len(str1) and j < len(str2):
            # Check if characters match or if the wrap-around condition is satisfied
            if str1[i] == str2[j] or (chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]):
                j += 1  #if a match increment both
            
            i += 1  #increment i either way

        # If we've successfully matched all characters in str2
        return j == len(str2)
        
