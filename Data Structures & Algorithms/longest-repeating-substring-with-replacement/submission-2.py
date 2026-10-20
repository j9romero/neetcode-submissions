class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        seen = defaultdict(int)
        l = 0

        for r in range(len(s)):
            seen[s[r]] += 1
            while r-l+1 - max(seen.values()) > k: 
                seen[s[l]] -= 1
                l +=1
            longest = max(longest, r-l+1)
        return longest