class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = defaultdict(int)
        have = defaultdict(int)

        for i in t:
            need[i] += 1
        
        required = len(need)
        formed = 0
        l = 0
        bestlen = float("inf")
        bestl = 0

        for r, char in enumerate(s):
            have[char] +=1
            if char in need and have[char] == need[char]:
                formed +=1
            while formed == required:
                if r-l +1 < bestlen:
                    bestlen = r-l+1
                    bestl = l
                leftchar = s[l]
                have[leftchar] -= 1
                if leftchar in need and have[leftchar] < need[leftchar]:
                    formed -= 1
                l +=1
        return "" if bestlen == float("inf") else s[bestl:bestl+bestlen]


        