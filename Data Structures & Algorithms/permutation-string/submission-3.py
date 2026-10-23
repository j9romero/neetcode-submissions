class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s1)
        k = len(s2)
        need = defaultdict(int)
        have = defaultdict(int)

        for i in s1:
            need[i] += 1
        
        for i, char in enumerate(s2):
            have[char] += 1
            if i >= n:
                have[s2[i-n]] -=1
                if have[s2[i-n]] <=0:
                    del have[s2[i-n]]
            if have == need:
                return True
        return False
