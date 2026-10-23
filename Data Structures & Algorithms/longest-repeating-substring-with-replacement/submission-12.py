class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = defaultdict(int)
        best = 0

        for r in range(len(s)):
            seen[s[r]] += 1
            while seen and ((r-l)+1) - max(seen.values()) > k and l<r:
                seen[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
            
        return best