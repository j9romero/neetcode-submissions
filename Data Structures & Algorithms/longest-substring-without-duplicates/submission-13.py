class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        r = 0
        best = 0

        for l in range(len(s)):
            while r< len(s) and s[r] not in seen:
                seen.add(s[r])
                r+=1
            best = max(best, r-l)
            seen.remove(s[l])
        return best
