class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash = [0]*26

        for letter in s:
            hash[(ord(letter)-ord('a'))] += 1
        
        for letter in t:
            hash[ord(letter)-ord('a')] -= 1

        if not any(hash):
            return True
        return False
        