class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        have = defaultdict(int)

        for i in t:
            need[i] += 1
        
        required = len(need)
        formed = 0
        l = 0
        best = float("inf")
        bestl = 0

        for r, char in enumerate(s):
            have[char] += 1
            if char in need and have[char] == need[char]:
                formed += 1
            while required == formed:
                if r-l + 1 < best:
                    best = r-l + 1
                    bestl = l

                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        return "" if best == float("inf") else s[bestl:bestl+best]
        
        