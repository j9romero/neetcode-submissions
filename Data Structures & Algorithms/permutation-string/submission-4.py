class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 

        need = defaultdict(int)
        have = defaultdict(int)

        for i in s1:
            need[i] += 1

        k = len(s1)
        for r, char in enumerate(s2):
            have[char] +=1
            if r >= k:
                left = s2[r-k] 
                have[left] -=1
                if have[left] == 0:
                    del have[left]
            if need == have:
                return True
        return False
        
