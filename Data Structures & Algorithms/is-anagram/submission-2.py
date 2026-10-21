class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = [0]*26
        seenT = [0]*26

        for i in s:
            seen[(ord(i)-ord('a'))] +=1
        
        for i in t:
            seenT[(ord(i)-ord('a'))] +=1
    
        if seen == seenT:
            return True
        return False 