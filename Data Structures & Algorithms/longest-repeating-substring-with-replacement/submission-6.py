class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        seen = defaultdict(int)

        for r in range(len(s)):
            seen[s[r]] +=1
            while seen and l<len(s) and ((r-l)+1) - max(seen.values(), default=0) > k:
                seen[s[l]] -=1
                l +=1
            w = (r-l) + 1
            longest = max(longest, w)
        return longest