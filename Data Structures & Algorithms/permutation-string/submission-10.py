class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = defaultdict(int)
        have = defaultdict(int)
        for i in s1:
            need[i] += 1

        l = 0
        required = len(need)
        for r, char in enumerate(s2):
            have[char]+=1
            if r >= len(s1):
                left = s2[r-len(s1)]
                have[left] -=1
                if have[left] == 0:
                    del have[left]
            if have == need:
                return True
        return False
        