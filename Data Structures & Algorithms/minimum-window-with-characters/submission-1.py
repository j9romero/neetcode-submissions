from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        have = defaultdict(int)
        need = defaultdict(int)

        for i in t:
            need[i] += 1

        required = len(need)
        formed = 0
        left = 0
        bestLen = float('inf')
        bestStart = 0

        for r, c in enumerate(s):
            have[c] += 1
            if c in need and have[c] == need[c]:
                formed += 1
            while formed == required:
                if r - left + 1 < bestLen:
                    bestLen = r - left + 1
                    bestStart = left
                l = s[left]
                have[l] -= 1
                if l in need and have[l] < need[l]:
                    formed -= 1
                left += 1

        return "" if bestLen == float('inf') else s[bestStart:bestStart + bestLen]
                