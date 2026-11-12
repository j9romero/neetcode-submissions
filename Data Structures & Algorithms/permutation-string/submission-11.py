class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = defaultdict(int)
        have = defaultdict(int)

        for i in s1:
            need[i] +=1 

        l = 0
        k = len(s1)
        for r, char in enumerate(s2):
            have[char] +=1
            if r >= k:
                have[s2[r-k]] -= 1
                if have[s2[r-k]] == 0:
                    del have[s2[r-k]]
            if have == need:
                return True
        return False

        