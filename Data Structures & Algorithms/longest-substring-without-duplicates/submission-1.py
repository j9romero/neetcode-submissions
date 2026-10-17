class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        best = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char]=i
            best = max(best, i-start+1)
        return best
        