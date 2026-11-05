class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l = 0
        need = defaultdict(int)
        have = defaultdict(int)

        for char in t:
            need[char] +=1

        needCount = len(need)
        formed = 0
        bestLen= float('inf')
        bestStart = 0
        for r, char in enumerate(s):
            have[char] += 1
            if char in need and have[char] ==need[char]:
                formed +=1
            while formed == needCount:
                if r - l +1 < bestLen:
                    bestLen = r-l+1
                    bestStart = l
                left = s[l]
                have[left] -= 1
                if left in need and have[left] < need[left]:
                    formed -= 1
                l +=1
        return "" if bestLen == float('inf') else s[bestStart:bestStart + bestLen]
        