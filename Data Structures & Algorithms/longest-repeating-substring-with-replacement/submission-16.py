class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        l = 0
        best = 0

        for r in range(len(s)):
            seen[s[r]] += 1
            while (r-l+1) - max(seen.values()) > k and l < len(s):
                seen[s[l]] -= 1
                l += 1
            window = (r-l) + 1
            best = max(best, window)
            
        return best 
        