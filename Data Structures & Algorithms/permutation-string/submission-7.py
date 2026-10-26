class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = defaultdict(int)
        have = defaultdict(int)

        for char in s1:
            need[char] += 1
        
        k = len(s1)

        for r, char in enumerate(s2):
            have[char] += 1
            if r >= k:
                left = s2[r-k]
                have[left] -= 1
                if have[left] == 0:
                    del have[left]
            if have == need:
                return True
            
        return False