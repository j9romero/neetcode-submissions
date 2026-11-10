class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens = [0] * 26
        seent = [0] *26

        for char in s:
            seens[ord(char) - ord('a')] +=1
        
        for char in t:
            seent[ord(char) - ord('a')] +=1
        
        if seens == seent:
            return True
        else:
            return False
        