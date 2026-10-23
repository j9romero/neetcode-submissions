class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        r = n-1
        seen = set()
        longest = 0

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l +=1
            longest = max(longest, (r-l)+1)
            seen.add(s[r])
        return longest

        